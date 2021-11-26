Group: System/Kernel and hardware
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:        Simple TTY terminal I/O application
Name:           tio
Version:        1.32
Release:        alt1_6
License:        GPLv2+
URL:            https://tio.github.io/
Source0:        https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-101BAC1C15B216DBE07A3EEA2BDB4A0944FA00B1.gpg
BuildRequires:  gnupg2
BuildRequires:  gcc
Source44: import.info

%description
Tio is a simple TTY terminal application which features a straightforward
commandline interface to easily connect to TTY devices for basic input/output.

%prep
%setup -q

%build
%configure --disable-silent-rules
%make_build

%install
%makeinstall_std

%files
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Nov 26 2021 Igor Vlasenko <viy@altlinux.org> 1.32-alt1_6
- do now own completions

* Sun Jun 30 2019 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1_1
- new version

