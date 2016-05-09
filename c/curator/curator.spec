Name: curator
Version: 3.5.1
Release: alt2
Summary: Tending your Elasticsearch indices

Group: Text tools
License: Apache2
Url: https://github.com/elastic/curator
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: python-module-setuptools python-module-urllib3 python-module-click

BuildArch: noarch

Requires: python-module-elasticsearch >= 2.3.0

%description
Like a museum curator manages the exhibits and collections on display,
Elasticsearch Curator helps you curate, or manage your indices.

%prep
%setup

%build
python setup.py build

%install
python setup.py install --root %buildroot

%files
%_bindir/%name
%_bindir/es_repo_mgr
%python_sitelibdir/%name
%python_sitelibdir/*.egg-info
%doc README.rst CONTRIBUTORS Dockerfile NOTICE CONTRIBUTING.md LICENSE.txt

%changelog
* Mon May  9 2016 Terechkov Evgenii <evg@altlinux.org> 3.5.1-alt2
- Update elasticsearch-py version requirement

* Mon May  9 2016 Terechkov Evgenii <evg@altlinux.org> 3.5.1-alt1
- Initial build for ALT Linux Sisyphus
