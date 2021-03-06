Summary: Jmatconvol is a real-time convolution engine.
Name:    jmatconvol
Version: 0.3.3
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/
Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: jack-audio-connection-kit-devel
BuildRequires: zita-convolver-devel
BuildRequires: libsndfile-devel
BuildRequires: clthreads-devel
BuildRequires: fftw-devel

%description
Jmatconvol is a real-time convolution engine. In
contrast to jconvolver it uses a single partition
size equal to the Jack period, and is optimised
for dense matrices of short convolutions, e.g.
for processing signals from spherical microphones
such as the Eigenmic. The maximum convolution
length is limited to 4096 samples in this release.

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile

pushd source
make PREFIX=%{_prefix}
popd

%install
pushd source
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/jmatconvol/config/
cp -r ../config_files/* $RPM_BUILD_ROOT%{_datadir}/jmatconvol/config/

make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS README* COPYING
%{_bindir}/*
%{_datadir}/jmatconvol/config/*

%changelog
* Fri Sep 17 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-1
- Initial build
