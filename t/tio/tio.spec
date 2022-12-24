Group: System/Kernel and hardware
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:        Simple TTY terminal I/O application
Name:           tio
Version:        2.5
Release:        alt1_1
License:        GPL-2.0-or-later
URL:            https://tio.github.io/
Source0:        https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/101BAC1C15B216DBE07A3EEA2BDB4A0944FA00B1
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  meson >= 0.53.2
BuildRequires:  libinih-devel
BuildRequires:  bash-completion
Source44: import.info

%description
Tio is a simple TTY terminal application which features a straightforward
commandline interface to easily connect to TTY devices for basic input/output.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%doc --no-dereference LICENSE
%doc AUTHORS NEWS README.md example/config
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 2.5-alt1_1
- update to new release by fcimport

* Tue Aug 02 2022 Igor Vlasenko <viy@altlinux.org> 1.47-alt1_1
- update to new release by fcimport

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 1.40-alt1_1
- update to new release by fcimport

* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 1.37-alt1_1
- update to new release by fcimport

* Fri Nov 26 2021 Igor Vlasenko <viy@altlinux.org> 1.32-alt1_6
- do now own completions

* Sun Jun 30 2019 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1_1
- new version

