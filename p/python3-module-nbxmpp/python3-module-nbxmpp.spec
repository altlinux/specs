%global modname nbxmpp
Name: python3-module-%modname
Version: 5.0.4
Release: alt1
Summary: Python library for non-blocking use of Jabber/XMPP
License: GPLv3+
Url: https://python-nbxmpp.gajim.org/
Group: Development/Python3

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: https://dev.gajim.org/gajim/python-nbxmpp/-/archive/nbxmpp-%version/python-nbxmpp-%version.tar.bz2
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel pyproject-build rpm-macros-python3 python3-module-build
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)


# python-nbxmpp 4.0.0 has been ported to libsoup3
Requires: libsoup3.0-gir

# does not work with gajim < 1.9
Conflicts: gajim < 1.9
Obsoletes: python3-nbxmpp-doc

%description
python-nbxmpp is a Python library that provides a way for Python applications
to use Jabber/XMPP networks in a non-blocking way.

Features:
- Asynchronous
- ANONYMOUS, EXTERNAL, GSSAPI, SCRAM-SHA-1, DIGEST-MD5, PLAIN, and
    X-MESSENGER-OAUTH2 authentication mechanisms.
- Connection via proxies
- TLS
- BOSH (XEP-0124)
- Stream Management (XEP-0198)


%prep
%setup -n python-%modname-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md ChangeLog
%python3_sitelibdir/%modname
%python3_sitelibdir/%modname-%version.dist-info

%changelog
* Tue Sep 24 2024 Ilya Mashkin <oddity@altlinux.ru> 5.0.4-alt1
- 5.0.4

* Tue Aug 13 2024 Ilya Mashkin <oddity@altlinux.ru> 5.0.3-alt1
- 5.0.3

* Sat Jul 20 2024 Ilya Mashkin <oddity@altlinux.ru> 5.0.2-alt1
- 5.0.2

* Mon Jun 24 2024 Ilya Mashkin <oddity@altlinux.ru> 5.0.1-alt1
- 5.0.1

* Wed Jun 12 2024 Ilya Mashkin <oddity@altlinux.ru> 5.0.0-alt1
- 5.0.0

* Mon Nov 27 2023 Ilya Mashkin <oddity@altlinux.ru> 4.5.3-alt1
- 4.5.3

* Sat Nov 11 2023 Ilya Mashkin <oddity@altlinux.ru> 4.5.2-alt1
- 4.5.2

* Tue Oct 31 2023 Ilya Mashkin <oddity@altlinux.ru> 4.5.0-alt1
- 4.5.0

* Thu Aug 31 2023 Ilya Mashkin <oddity@altlinux.ru> 4.3.3-alt1
- 4.3.3

* Tue May 30 2023 Ilya Mashkin <oddity@altlinux.ru> 4.3.1-alt1
- 4.3.1

* Sun May 28 2023 Ilya Mashkin <oddity@altlinux.ru> 4.3.0-alt1
- 4.3.0

* Tue Apr 04 2023 Ilya Mashkin <oddity@altlinux.ru> 4.2.2-alt1
- 4.2.2

* Mon Feb 06 2023 Ilya Mashkin <oddity@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Sun Feb 05 2023 Ilya Mashkin <oddity@altlinux.ru> 4.1.0-alt1
- 4.1.0

* Mon Jan 16 2023 Ilya Mashkin <oddity@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Wed Jan 11 2023 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.0-alt2
- Added missing requires to libsoup3.0-gir

* Tue Jan 10 2023 Ilya Mashkin <oddity@altlinux.ru> 4.0.0-alt1
- 4.0.0
- Obsoletes:  python-nbxmpp-doc

* Tue Nov 01 2022 Ilya Mashkin <oddity@altlinux.ru> 3.2.5-alt1
- 3.2.5

* Mon Oct 10 2022 Ilya Mashkin <oddity@altlinux.ru> 3.2.4-alt1
- 3.2.4

* Tue Oct 04 2022 Ilya Mashkin <oddity@altlinux.ru> 3.2.3-alt1
- 3.2.3

* Sat Sep 24 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.2.2-alt1
- NMU: 3.2.2 (Closes: #43856)

* Sat Sep 10 2022 Ilya Mashkin <oddity@altlinux.ru> 3.2.1-alt1
- 3.2.1

* Sat Jul 30 2022 Ilya Mashkin <oddity@altlinux.ru> 3.1.1-alt1
- 3.1.1

* Sat Jun 18 2022 Ilya Mashkin <oddity@altlinux.ru> 3.1.0-alt1
- 3.1.0

* Sun May 22 2022 Ilya Mashkin <oddity@altlinux.ru> 3.0.2-alt1
- 3.0.2

* Sun May 22 2022 Ilya Mashkin <oddity@altlinux.ru> 3.0.2-alt1
- 3.0.2

* Sat May 14 2022 Ilya Mashkin <oddity@altlinux.ru> 3.0.1-alt1
- 3.0.1

* Thu Mar 17 2022 Ilya Mashkin <oddity@altlinux.ru> 2.0.6-alt1
- 2.0.6

* Mon Oct 18 2021 Ilya Mashkin <oddity@altlinux.ru> 2.0.4-alt1
- 2.0.4 (Closes: #41133)

* Wed Mar 10 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.0.2-alt1
- 2.0.2
- Updated source url.
- Conflicts with gajim < 1.3

* Mon Oct 19 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.0.2-alt1
- 1.0.2
- spec: fix license field

* Sun Aug 18 2019 Alexey Shabalin <shaba@altlinux.org> 0.6.10-alt1
- 0.6.10

* Fri Oct 19 2018 Ilya Mashkin <oddity@altlinux.ru> 0.6.8-alt1
- 0.6.8

* Tue May 15 2018 Ilya Mashkin <oddity@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Tue Dec 12 2017 Ilya Mashkin <oddity@altlinux.ru> 0.6.1-alt1
- 0.6.1 (Closes: #34321)

* Sat Dec 09 2017 Ilya Mashkin <oddity@altlinux.ru> 0.5.6-alt1
- 0.5.6

* Sat Feb 18 2017 Ilya Mashkin <oddity@altlinux.ru> 0.5.5-alt1
- 0.5.5

* Sat Sep 12 2015 Ilya Mashkin <oddity@altlinux.ru> 0.5.3-alt1
- 0.5.3

* Tue Apr 17 2014 Ilya Mashkin <oddity@altlinux.ru> 0.4-alt1
- Build for Sisyphus

* Wed Mar 19 2014 Michal Schmidt <mschmidt@redhat.com> - 0.4-1
- Initial Fedora packaging.
