# Global variables for github repository
%global commit0 7232969a1d02eea926ab5592d2a0bc0c54003d05
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:           zam-plugins
Version:        3.10
Release:        1%{?dist}
Summary:        Zam LV2 set of plugins

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/zamaudio/zam-plugins
# in the zam repository -> make dist
Source0:        zam-plugins-3.10-10-g7232969.tar.xz

BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libsamplerate-devel

%description
Zam LV2 set of plugins

%package -n ladspa-zam
Summary:        Zam LADSPA plugin
Group:          Applications/Multimedia

%description -n ladspa-zam
Zam LADSPA plugin

%package -n vst-zam
Summary:        Zam VST plugin
Group:          Applications/Multimedia

%description -n vst-zam
Zam VST plugin

%prep
%setup -qn zam-plugins-3.10-10-g7232969

%build
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} all

%install 
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} install

%files
%{_bindir}/*
%{_libdir}/lv2/*

%files -n ladspa-zam
%{_libdir}/ladspa/* 

%files -n vst-zam
%{_libdir}/vst/* 

%changelog
* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 3.10
- update version to 3.10
* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 3.9
- update version to 3.9
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 3.5
- Initial build
