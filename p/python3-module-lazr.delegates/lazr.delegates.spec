%define _unpackaged_files_terminate_build 1
%define oname lazr.delegates

%def_with check

Name: python3-module-%oname
Version: 2.1.0
Release: alt1

Summary: Easily write objects that delegate behavior
License: LGPLv3
Group: Development/Python3
Url: https://pypi.org/project/lazr.delegates
Vcs: https://launchpad.net/lazr.delegates

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-zope.testrunner
%endif

%description
The lazr.delegates package makes it easy to write objects that delegate behavior
to another object. The new object adds some property or behavior on to the other
object, while still providing the underlying interface, and delegating behavior.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%tox_check

%files
%doc *.rst *.txt
%python3_sitelibdir/lazr
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests


%changelog
* Wed Mar 22 2023 Anton Vyatkin <toni@altlinux.org> 2.1.0-alt1
- New version 2.1.0.

* Fri Feb 22 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.4-alt2
- Broken reqs for p8 branch fixed

* Fri Feb 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.4-alt1
- Initial build for Sisyphus
