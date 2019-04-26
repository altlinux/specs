%define oname sphinxcontrib-serializinghtml

Name:           python3-module-%oname
Version:        1.1.3
Release:        alt1

Summary:        Sphinx extension for serialized HTML

Group:          Development/Python3
License:        BSD
URL:            https://pypi.org/project/sphinxcontrib-serializinghtml

Source0:        %oname-%version.tar

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python3-dev
BuildRequires:  python3-module-setuptools

%description
sphinxcontrib-serializinghtml is a sphinx extension which outputs "serialized"
HTML files (json and pickle).

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/sphinxcontrib/
%python3_sitelibdir/*.pth
%python3_sitelibdir/*.egg-info/

%changelog
* Thu Apr 25 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus.
