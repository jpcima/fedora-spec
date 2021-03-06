Summary: Yet Another Scrolling Scope. Main features: up to 32 channels, variable scrolling speed, automatic gain control, and very light on CPU usage. Beta release available.
Name:    yass
Version: 0.1.0
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/
Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: clthreads-devel clxclient-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel libXft-devel

%description
Yet Another Scrolling Scope. Main features: up to 32 channels, variable scrolling speed, automatic gain control, and very light on CPU usage. Beta release available.

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
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/
cp .yassrc $RPM_BUILD_ROOT%{_datadir}/doc/yassrc.sample

pushd source
make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS README COPYING
%{_bindir}/*
%{_docdir}/*

%changelog
* Fri Sep 7 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- initial release
