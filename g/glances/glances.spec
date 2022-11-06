%define _unpackaged_files_terminate_build 1

Name: glances
Version: 3.3.0.4
Release: alt1

Summary: CLI curses based monitoring tool
License: GPLv3
Group: Monitoring
Url: https://github.com/nicolargo/glances
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

Requires: python3-module-%name = %EVR

#skip findreq for optional dependencies from exports
%add_findreq_skiplist %python3_sitelibdir/%name/exports/*.py

%if 0%{?!_without_check:1} && 0%{?!_disable_check:1}
BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-psutil
BuildRequires: /proc
%endif


%description
Glances is a CLI curses based monitoring tool for both GNU/Linux and BSD.

Glances uses the PsUtil library to get information from your system.

%package -n python3-module-%name
Summary: CLI curses based monitoring tool
Group: Development/Python3
Requires: python3(defusedxml.xmlrpc)

%description -n python3-module-%name
Glances is a CLI curses based monitoring tool for both GNU/Linux and BSD.

Glances uses the PsUtil library to get information from your system.

%prep
%setup

%patch0 -p1

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%_bindir/glances
%_man1dir/glances.1*
%_docdir/glances/

%files -n python3-module-%name
%doc AUTHORS COPYING README.rst NEWS.rst
%python3_sitelibdir/%name/
%python3_sitelibdir/Glances-%version-py%_python3_version.egg-info/


%changelog
* Sun Nov 06 2022 Egor Ignatov <egori@altlinux.org> 3.3.0.4-alt1
- new version 3.3.0.4

* Sun Oct 30 2022 Egor Ignatov <egori@altlinux.org> 3.3.0.2-alt1
- new version 3.3.0.2

* Tue Oct 18 2022 Egor Ignatov <egori@altlinux.org> 3.3.0.1-alt1
- new version 3.3.0.1

* Fri Jul 29 2022 Egor Ignatov <egori@altlinux.org> 3.2.7-alt1
- new version 3.2.7

* Mon Jun 20 2022 Egor Ignatov <egori@altlinux.org> 3.2.6.4-alt2
- remove 'future' and 'packaging' dependencies (9b9a7862)
  + future is python2 only dependency
  + packaging is optional and used to check for updates

* Tue May 31 2022 Egor Ignatov <egori@altlinux.org> 3.2.6.4-alt1
- new version 3.2.6.4

* Wed May 25 2022 Egor Ignatov <egori@altlinux.org> 3.2.6.1-alt1
- new version 3.2.6.1

* Mon Apr 11 2022 Egor Ignatov <egori@altlinux.org> 3.2.5-alt1
- new version 3.2.5

* Wed Dec 01 2021 Egor Ignatov <egori@altlinux.org> 3.2.4.2-alt1
- new version

* Wed Aug 25 2021 Egor Ignatov <egori@altlinux.org> 3.2.3.1-alt1
- new version

* Tue Aug 17 2021 Egor Ignatov <egori@altlinux.org> 3.2.3-alt1
- new version

* Fri Jul 09 2021 Egor Ignatov <egori@altlinux.org> 3.2.0-alt1
- new version

* Fri May 14 2021 Egor Ignatov <egori@altlinux.org> 3.1.7-alt1
- new version

* Mon Apr 26 2021 Egor Ignatov <egori@altlinux.org> 3.1.6-alt1
- new version

* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.11.1-alt2
- build for python2 disabled

* Wed Oct 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.11.1-alt1
- Initial build.
