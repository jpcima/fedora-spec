Summary: Jack_utils contains three small command line programs: jack_fpmon, jack_check, jack_proxy
Name:    jack_utils
Version: 0.0.1
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/
Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: jack-audio-connection-kit-devel

%description
jack_utils contains three small command line programs.

jack_fpmon: watch an audio signal for denormals, Nan and Inf samples.

jack_check: watch for discontinuities in Jack's timing info (frametime
   and period start times). This has been quite useful while developing
   zita-njbridge.

jack_proxy: this just copies inputs to outputs. There are some Jack
   clients which autoconnect to the system:playback ports and provide
   no other options. There's little that can be done about those.
   There are some others which at least allow you to specify a client
   to connect to - but not to which ports. They just make a random
   choice and this of course fails completely when the client has
   multiple sets of ports with different functions.
   It is for these that jack-proxy can be handy. Just run a jack_proxy
   with the number of ports you need and connect them to your client(s).
   Then tell the broken app to connect to the proxy.

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile
sed -i 's|-lasound||' source/Makefile

pushd source
make PREFIX=%{_prefix}
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}/

pushd source
make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS README COPYING
%{_bindir}/*

%changelog
* Fri Sep 7 2018 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- initial release
