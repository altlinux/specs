%define oname bzr-fastimport
Name: python-module-bzr-fastimport
Version: 0.13.0
Release: alt4%ubt
Summary: Bazaar Fast Import is a plugin for loading of revision control data

Packager: Ildar Mulyukov <ildar@altlinux.ru>

BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version.patch
Group: Development/Other
Url: https://launchpad.net/bzr-fastimport
License: GPL2

BuildRequires(pre): rpm-build-ubt
BuildRequires: python-devel

%description
It is designed to be used in combination with front-end programs
that generate a command/data stream for it to process. Front-ends
are available for a wide range of foreign VCS tools including Subversion,
CVS, Git, Mercurial, Darcs and Perforce. New front-ends are easy
to develop in whatever programming language you prefer,
making Bazaar Fast Import useful for teams needing a custom migration solution.

%package -n python-module-bzr-fastimport-tests
Summary: Bzr-fastimport plugin tests
Group: Development/Other

Requires: %name = %version-%release

%description -n python-module-bzr-fastimport-tests
This package contain tools and test suites for testing bzr-fastimport.

%prep
%setup
%patch -p1

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir

%files
%python_sitelibdir/bzrlib/plugins/fastimport
%exclude %python_sitelibdir/bzrlib/plugins/fastimport/tests
%python_sitelibdir/bzr_fastimport-*egg-info
%doc doc/* NEWS README.txt

%files -n python-module-bzr-fastimport-tests
%dir %python_sitelibdir/bzrlib/plugins/fastimport
%python_sitelibdir/bzrlib/plugins/fastimport/tests

%changelog
* Fri Dec 01 2017 Anatoly Kitaykin <cetus@altlinux.org> 0.13.0-alt4%ubt
- upstream snapshot (fixed work with python-module-fastimport-0.9.6)

* Thu Sep 28 2017 Alexey Shabalin <shaba@altlinux.ru> 0.13.0-alt3%ubt
- fixed lp bug 1607974
- fixed lp bug 1295833

* Thu Sep 18 2014 Alexey Shabalin <shaba@altlinux.ru> 0.13.0-alt2
- upstream snapshot (fixed work with python-module-fastimport-0.9.4)

* Fri Mar 09 2012 Anatoly Kitaikin <cetus@altlinux.org> 0.13.0-alt1
- new version
- subpackage python-module-bzr-fastimport-tests

* Mon Feb 27 2012 Anatoly Kitaikin <cetus@altlinux.org> 0.12.0-alt1
- new version

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.0-alt1.1
- Rebuild with Python-2.7

* Wed Oct 12 2011 Anatoly Kitaikin <cetus@altlinux.org> 0.11.0-alt1
- new version

* Sun Jul 18 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.8.0_483_g514ae4f-alt1
- new version
- based on original VCS tree converted with itself to GIT
- noarch
- closes ALT bug 23773

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.1
- Rebuilt with python 2.6

* Sun Mar 01 2009 Boris Savelev <boris@altlinux.org> 0.6-alt1
- initial build for Sisyphus
