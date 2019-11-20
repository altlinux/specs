Name: alsa-ucm-conf
Version: 1.2.1
Release: alt1

Summary: Advanced Linux Sound Architecture (ALSA) Use Case Manager data
License: BSD
Group: System/Libraries

Url: http://www.alsa-project.org
Source: %name-%version.tar
BuildArch: noarch

%define alsadata %_datadir/alsa

%description
Advanced Linux Sound Architecture (ALSA) Use Case Manager data
used to sit in libalsa but have been factored out to be maintained
in a standalone repository.

%prep
%setup

%build

%install
mkdir -p %buildroot%alsadata
cp -at %buildroot%alsadata -- ucm*

%files
%alsadata/*
%doc LICENSE

%changelog
* Mon Nov 18 2019 Michael Shigorin <mike@altlinux.org> 1.2.1-alt1
- initial release

