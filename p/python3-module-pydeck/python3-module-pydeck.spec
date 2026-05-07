%define pypi_name pydeck

Name: python3-module-%pypi_name
Version: 0.9.2
Release: alt1

Summary: Widget for deck.gl maps

License: Apache-2.0
Group: Development/Python3
URL: https://github.com/visgl/deck.gl/tree/master/bindings/pydeck
# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
pydeck is a set of Python bindings for making spatial visualizations with
deck.gl, optimized for a Jupyter environment. It is used by Streamlit
(st.pydeck_chart) and Jupyter notebooks for large-scale interactive data
visualization in Python.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# pip installs data_files with relative paths under %_prefix; move config to /etc
mkdir -p %buildroot%_sysconfdir/jupyter/nbconfig/notebook.d
mv -v %buildroot%_prefix/etc/jupyter/nbconfig/notebook.d/%pypi_name.json \
      %buildroot%_sysconfdir/jupyter/nbconfig/notebook.d/
rm -rv %buildroot%_prefix/etc

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_datadir/jupyter/nbextensions/%pypi_name/
%_sysconfdir/jupyter/nbconfig/notebook.d/%pypi_name.json

%changelog
* Tue May 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- initial build for ALT Sisyphus

