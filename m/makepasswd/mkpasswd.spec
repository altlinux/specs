Summary: Tool to generate password/passwords hash
Name: makepasswd
Version: 0.5.3
Release: alt1.3
Url: http://people.defora.org/~khorben/projects/makepasswd/
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: GPLv2
Group: System/Base

BuildRequires: libssl-devel xsltproc docbook-style-xsl alt-docs-xsl-manpages docbook-dtds
Source: %name-%version.tar
Patch0: makepasswd-0.5.3-alt1-link-fixes.patch
Patch1: makepasswd-0.5.3-alt1-sbin-fix.patch

%description
Makepasswd generates (pseudo-)random passwords of a desired length.
It is able to generate its crypted equivalent.

%prep
%setup
%patch0 -p1
%patch1 -p1


%build
%make

%install
%makeinstall_std PREFIX=/usr

%files
%doc doc/makepasswd.html
%_sbindir/*
%_man1dir/*


%changelog
* Mon Jan 28 2019 Ivan A. Melnikov <iv@altlinux.org> 0.5.3-alt1.3
- NMU: fix build with recent docbook-style-xsl

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.5.3-alt1.2
- NMU: Rebuild with new openssl 1.1.0.

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1.1
- NMU: cleaned up unused BR: docbook-xml

* Thu Jun 19 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.3-alt1
- New version

* Tue Feb 19 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.1-alt1
- Initial build

