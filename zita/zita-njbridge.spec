Summary: Full quality multichannel audio over a local IP network
Name:    zita-njbridge
Version: 0.4.2
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/
Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: jack-audio-connection-kit-devel
BuildRequires: zita-resampler-devel

%description
Command line Jack clients to transmit full quality multichannel audio
over a local IP network, with adaptive resampling by the
receiver(s). Zita-njbridge can be used for a one-to-one connection
(using UDP) or in a one-to-many system (using multicast). Sender and
receiver(s) can each have their own sample rate and period size, and
no word clock sync between them is assumed. Up 64 channels can be
transmitted, receivers can select any combination of these. On a
lightly loaded or dedicated network zita-njbridge can provide low
latency (same as for an analog connection). Additional buffering can
be specified in case there is significant network delay jitter. IPv6
is fully supported.

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
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
pushd source
make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS README* 
%{_bindir}/zita-*
%{_mandir}/man1/*

%changelog
* Fri Aug 17 2018 Yann Collette <ycollette.nospam@free.fr> - 0.4.2-1
- update to 0.4.2.0

* Wed Aug  6 2014 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.0-1
- initial build.
