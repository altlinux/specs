%define _unpackaged_files_terminate_build 1
%define modname dnstwist

Name: python3-module-%modname
Version: 20250130
Release: alt1

Summary: Domain name permutation engine for detecting phishing and typo squatting

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/dnstwist/
Vcs: https://github.com/elceef/dnstwist

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

Requires: python3-module-dns
Requires: python3-module-idna

Provides: %modname = %EVR

%description
dnstwist generates a list of domain names that look similar to the given one
and checks whether any of them is registered. It helps to detect homograph
phishing attacks, typo squatting and brand impersonation.

Besides generating permutations, dnstwist can resolve addresses, fetch
WHOIS/GeoIP data, compare web page fuzzy hashes and export results as CSV
or JSON.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
install -Dpm0644 docs/%modname.1 %buildroot%_man1dir/%modname.1

%files
%doc docs/README.md docs/THANKS.md LICENSE
%_bindir/%modname
%_man1dir/%modname.1*
%python3_sitelibdir/%modname.py
%python3_sitelibdir/__pycache__/%modname.*
%python3_sitelibdir/%modname-%version.dist-info

%changelog
* Wed Sep 16 2026 Denis Rastyogin <gerben@altlinux.org> 20250130-alt1
- Initial build for ALT Linux.
