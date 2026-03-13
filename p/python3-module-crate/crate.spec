%define   modulename crate
%def_with check

Name:     python3-module-%modulename
Version:  2.1.2
Release:  alt1

Summary:  Python DB API client library for CrateDB, using HTTP

License:  Apache-2.0
Group:    Development/Python3
URL:      https://pypi.org/project/crate
VCS:      https://github.com/crate/crate-python

BuildArch: noarch

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-versioningit
BuildRequires: git

%if_with check
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-orjson
BuildRequires: python3-module-certifi
BuildRequires: python3-module-pytz
%endif

%description
%summary.

%prep
%setup

if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m "release"
    git tag "%version"
fi

# Drop dependency on verlib2 crap
grep -rl "from verlib2" | xargs sed -i 's/verlib2/packaging.version/'
sed -i 's/version.version/version.release/' tests/client/test_connection.py

%build
%pyproject_build

%install
%pyproject_install

mv -v %buildroot%python3_sitelibdir/%modulename-%version+*.dist-info \
     %buildroot%python3_sitelibdir/%modulename-%version.dist-info

%check
# These tests need network:
# test_docs
# test_additional_settings
# test_basic
# test_cluster
# test_default_settings
# test_dynamic_http_port
# test_environment_variables
# test_verbosity
# test_layer_from_uri
%pyproject_run_pytest -k"not test_docs \
and not test_additional_settings \
and not test_basic \
and not test_cluster \
and not test_default_settings \
and not test_dynamic_http_port \
and not test_environment_variables \
and not test_verbosity \
and not test_layer_from_uri"

%files
%doc LICENSE README.rst CHANGES.rst
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Fri Mar 13 2026 Grigory Ustinov <grenka@altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus.
