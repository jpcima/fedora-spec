%global debug_package %{nil}

# Global variables for github repository
%global commit0 1967b550527dcfa11e334b08b65da9cf7cc68660
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           Carla
Version:        2.0.0.%{shortcommit0}
Release:        5%{?dist}
Summary:        A rack manager JACK

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/falkTX/Carla
Source0:        https://github.com/falkTX/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

Patch0:         carla-0001-change-default-path.patch

BuildRequires: python-qt5-devel
BuildRequires: python-magic
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: qt-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: fluidsynth-devel
BuildRequires: fftw-devel
BuildRequires: mxml-devel
BuildRequires: zlib-devel
BuildRequires: mesa-libGL-devel
BuildRequires: non-ntk-fluid
BuildRequires: non-ntk-devel
BuildRequires: jack-audio-connection-kit-devel
#BuildRequires: linuxsampler-devel
#BuildRequires: libprojectM-devel

Requires(pre): python3-qt5

%description
A rack manager for JACK

%prep
%setup -qn %{name}-%{commit0}

%patch0 -p1 

%build
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_libdir} %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_libdir}  %{?_smp_mflags} install

# Create a vst directory
%__install -m 755 -d %{buildroot}/%{_libdir}/vst/

%post 
update-desktop-database -q
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :

%postun
update-desktop-database -q
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi

%posttrans 
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{_bindir}/*
%{_includedir}/carla/*
%{_libdir}/carla/*
%{_libdir}/lv2/*
%{_libdir}/pkgconfig/*
%{_libdir}/python3/*
%{_libdir}/vst/
%{_datadir}/applications/*
%{_datadir}/carla/*
%{_datadir}/icons/*
%{_datadir}/mime/*

%changelog
* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 2.0.0beta-5
- update to latest master
* Tue May 1 2018 Yann Collette <ycollette.nospam@free.fr> - 2.0.0beta-4
- version 4
- update default folders
- update to master
* Wed Nov 22 2017 Yann Collette <ycollette.nospam@free.fr> - 2.0.0beta
- add a missing requires
* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 2.0.0beta
- update to latest master
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 2.0.0beta
- Initial build
