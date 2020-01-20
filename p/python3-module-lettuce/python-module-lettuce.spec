%define oname lettuce

Name: python3-module-%oname
Version: 0.2.23
Release: alt1

Summary: Behaviour Driven Development for Python
License: GPLv3+
Group: Development/Python3
URL: http://lettuce.it/
BuildArch: noarch

Source: %oname-%version.tar
Patch0: fix-import.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-fuzzywuzzy
BuildRequires: python3-module-mock
BuildRequires: python3-module-mox
BuildRequires: python3-module-nose
BuildRequires: python-tools-2to3

Requires: python3-module-sure

Conflicts: python-module-%oname


%description
Lettuce is an extremely useful and charming tool for BDD (Behavior
Driven Development). It can execute plain-text functional descriptions
as automated tests for Python projects, just as Cucumber does for Ruby.

Lettuce makes the development and testing process really easy, scalable,
readable and - what is best - it allows someone who doesn't program to
describe the behavior of a certain system, without imagining those
descriptions will automatically test the system during its development.

%prep
%setup -n %oname-%version
%patch0 -p1

pushd %oname
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
popd

%build
%python3_build

%install
%python3_install

%check
%if 0
export PYTHONPATH=`pwd`
nosetests3 -s tests/unit
nosetests3 -s tests/functional
%endif

%files
%doc COPYING README.md
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/%oname/django/tests
%python3_sitelibdir/*.egg-info


%changelog
* Mon Jan 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.23-alt1
- Version updated to 0.2.23
- porting on python3.

* Sat Mar 30 2013 Ivan A. Melnikov <iv@altlinux.org> 0.2.16-alt1
- New version.

* Sat Feb 09 2013 Ivan A. Melnikov <iv@altlinux.org> 0.2.14-alt2
- Exclude test for integration with django from package.

* Sat Feb 09 2013 Ivan A. Melnikov <iv@altlinux.org> 0.2.14-alt1
- New version.

* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.2.11-alt1
- New version;
- Correct description.

* Sun Nov 04 2012 Ivan A. Melnikov <iv@altlinux.org> 0.2.10-alt1.git36ffa10
- Initial build for Sisyphus.

