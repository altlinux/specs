%global modname nbxmpp
Name: python3-module-%modname
Version: 4.1.0
Release: alt1
Summary: Python library for non-blocking use of Jabber/XMPP
License: GPLv3+
Url: https://python-nbxmpp.gajim.org/
Group: Development/Python3

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: https://dev.gajim.org/gajim/python-nbxmpp/-/archive/nbxmpp-%version/python-nbxmpp-%version.tar.bz2
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools pyproject-build rpm-macros-python3 python3-module-build

# python-nbxmpp 4.0.0 has been ported to libsoup3
Requires: libsoup3.0-gir

# does not work with gajim < 1.6
Conflicts: gajim < 1.7
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
# https://bugzilla.altlinux.org/show_bug.cgi?id=39907
[ -e setup.py ] && rm -f ./setup.py
echo 'import setuptools; setuptools.setup()' > setup.py

%build
%python3_build

%install
%python3_install

%files
%doc README.md ChangeLog
%python3_sitelibdir/%modname
%python3_sitelibdir/%modname-%version-*.egg-info

%changelog
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
