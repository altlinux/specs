%global pypi_name bootstrap3

Name:           python3-module-django-%pypi_name
Version:        12.0.1
Release:        alt1.1

Summary:        Bootstrap support for Django projects
License:        Apache
Group:          Development/Python3
URL:            https://pypi.python.org/pypi/django-bootstrap3
BuildArch:      noarch

Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm python3-module-django


%description
Write Django as usual, and let django-bootstrap3 make template output into Bootstrap 3 code

%package tests
Summary: Tests %pypi_name
Group: Development/Python3
Requires: %name = %EVR

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%pypi_name/tests/

%description tests
Write Django as usual, and let django-bootstrap3 make template output into Bootstrap 3 code

This package contains tests for %name.

%prep
%setup

%build
%python3_build

%install
%python3_install

mv tests/ %buildroot%python3_sitelibdir/%pypi_name/

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%files
%doc *.rst docs/ example/
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%pypi_name/tests

%files tests
%python3_sitelibdir/%pypi_name/tests/


%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 12.0.1-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 12.0.1-alt1
- Version updated to 12.0.1
- build for python2 disabled

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 8.2.3-alt2.qa1
- NMU: applied repocop patch

* Thu Jun 01 2017 Lenar Shakirov <snejok@altlinux.ru> 8.2.3-alt2
- Pack correct sources

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 8.2.3-alt1
- Initial build for ALT

