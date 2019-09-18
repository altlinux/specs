Name:		codespell
Version:	1.16.0.0.5.g8b321f0
Release:	alt1
Summary:	Check code for common misspellings
Group:		Development/Tools
License:	GPLv2
URL:		https://github.com/codespell-project/codespell
Source:		%name-%version.tar
BuildArch:	noarch

BuildRequires(pre): rpm-build-python3
BuildRequires:	python3-devel
BuildRequires:	python3-module-setuptools
BuildRequires:	help2man

%description
Fix common misspellings in text files. It's designed primarily for checking
misspelled words in source code, but it can be used with other files as well.

%prep
%setup -q
subst 's/help2man/& -L en_US.UTF-8 --no-discard-stderr/' Makefile

%build
make
%python3_build

%install
%python3_install
install -D -m644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc TODO COPYING README.rst
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%python3_sitelibdir/*

%changelog
* Wed Sep 18 2019 Vitaly Chikunov <vt@altlinux.org> 1.16.0.0.5.g8b321f0-alt1
- Build v1.16.0-5-g8b321f0

* Thu Oct 04 2018 Vitaly Chikunov <vt@altlinux.ru> 1.14.0-alt1
- First packaging for ALT
