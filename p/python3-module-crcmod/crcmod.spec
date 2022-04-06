#global debug_package %{nil}

%define oname crcmod

Name:    python3-module-%oname
Version: 1.7
Release: alt1
Summary: CRC Generator
Group:   Development/Python3

License: MIT
URL:     http://crcmod.sourceforge.net/

# Source-url: %__pypi_url %oname
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-dev
#BuildRequires: python3-docs
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx

%description
%summary.

%package doc
Summary: Documentation for crcmod
Group: Documentation

BuildArch: noarch

%description doc
%summary.

%prep
%setup -n %oname-%version

# Use local intersphinx inventory
sed -r \
    -e 's|http://docs.python.org|%{_docdir}/python3-module-%oname-doc/|' \
    -i docs/source/conf.py

%build
%python3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

%check
for test in test/*; do
  PYTHONPATH="%buildroot%python3_sitelibdir" %__python3 $test
done

%files
%doc README changelog
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py3.*.egg-info

%files -n python3-module-%oname-doc
%doc html/*

%changelog
* Wed Apr 06 2022 Anton Midyukov <antohami@altlinux.org> 1.7-alt1
- Initial build for Sisyphus
