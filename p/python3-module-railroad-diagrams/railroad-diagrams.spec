Name:       python3-module-railroad-diagrams
Version:    1.1.1
Release:    alt1
Summary:    A small library for generating railroad diagrams using SVG
Group:      Development/Python3
BuildArch:  noarch
Source:     railroad-diagrams-%version.tar.gz
License:    MIT

# Automatically added by buildreq on Wed Feb 02 2022
# optimized out: libgpg-error python3 python3-base python3-dev python3-module-pkg_resources sh4
BuildRequires: python3-module-setuptools

%description
This is a small library for generating railroad diagrams (like what
JSON.org uses) using SVG, with both JS and Python ports.

Railroad diagrams are a way of visually representing a grammar in a form
that is more readable than using regular expressions or BNF. They can
easily represent any context-free grammar, and some more powerful
grammars. There are several railroad-diagram generators out there, but
none of them had the visual appeal I wanted, so I wrote my own.

See also https://github.com/tabatkins/railroad-diagrams for JS version

%prep
%setup -n railroad-diagrams-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Wed Feb 02 2022 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Initial build for ALT
