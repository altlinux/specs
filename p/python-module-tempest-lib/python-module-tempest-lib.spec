Name: python-module-tempest-lib
Version: 1.0.0
Release: alt1
Summary: OpenStack Functional Testing Library
Group: Development/Python

License: ASL 2.0
Url: http://www.openstack.org/
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: rpm-build-python
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: dos2unix
Requires: python-module-babel
Requires: python-module-fixtures
Requires: python-module-iso8601
Requires: python-module-jsonschema
Requires: python-module-httplib2
Requires: python-module-oslo-context >= 0.2.0
Requires: python-module-oslo-log >= 1.8.0
Requires: python-module-oslo-config >= 1.9.3
Requires: python-module-oslo-utils >= 1.4.0
Requires: python-module-oslo-i18n >= 1.5.0
Requires: python-module-oslo-serialization >= 1.4.0
Requires: python-module-oslo-concurrency >= 1.8.0
Requires: python-module-os-testr >= 0.1.0
Requires: python-module-paramiko

%description
Library for creating test suites for OpenStack projects.

%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation for %name

%prep
%setup
# Remove bundled egg-info
rm -rf *.egg-info

# remove shebangs and fix permissions
find -type f -a \( -name '*.py' -o -name 'py.*' \) \
   -exec sed -i '1{/^#!/d}' {} \; \
   -exec chmod u=rw,go=r {} \;

%build
%python_build
# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
dos2unix html/_static/jquery.js

%install
%python_install
# workaround for https://bugs.launchpad.net/tempest/+bug/1555825
rm %buildroot%_bindir/skip-tracker
rm %buildroot%_bindir/check-uuid

%files
%doc README.rst HACKING.rst AUTHORS ChangeLog CONTRIBUTING.rst
%python_sitelibdir/tempest_lib
%python_sitelibdir/tempest_lib-*-py?.?.egg-info

%files doc
%doc html doc/source/readme.rst

%changelog
* Mon Nov 14 2016 Lenar Shakirov <snejok@altlinux.ru> 1.0.0-alt1
- Initial build for ALT (based on CentOS 1.0.0-1.el7.src)

