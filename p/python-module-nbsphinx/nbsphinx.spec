%define oname nbsphinx
%def_with python3
%def_without docs

Name:           python-module-%oname
Version:        0.2.15
Release:        alt1
Summary:        Jupyter Notebook Tools for Sphinx

License:        MIT
Group: Development/Python
BuildArch:      noarch
URL:            http://nbsphinx.rtfd.io/

# https://github.com/spatialaudio/nbsphinx.git
Source:        %name-%version.tar

# https://github.com/spatialaudio/nbsphinx/issues/24
Patch0:         %oname-fedora-ipython-console-highlighting.patch
Patch1:         %oname-%version-alt-docversion.patch

BuildRequires:  python-module-setuptools
BuildRequires:  python-module-ipykernel
BuildRequires:  python-module-jupyter_client
BuildRequires:  python-module-nbconvert
BuildRequires:  python-module-sphinx
BuildRequires:  python-module-pathlib2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-ipykernel
BuildRequires:  python3-module-jupyter_client
BuildRequires:  python3-module-nbconvert
BuildRequires:  python3-module-sphinx
BuildRequires:  python3-module-pathlib2
%endif
%if_with docs
BuildRequires:  pandoc
%endif

%description
nbsphinx is a Sphinx extension that provides a source parser for *.ipynb
files. Custom Sphinx directives are used to show Jupyter Notebook code cells
(and of course their results) in both HTML and LaTeX output. Unevaluated
notebooks, i.e. notebooks without stored output cells, will be automatically
executed during the Sphinx build process.

%if_with python3
%package -n     python3-module-%oname
Summary:        Jupyter Notebook Tools for Sphinx
Group: Development/Python3

%description -n python3-module-%oname
nbsphinx is a Sphinx extension that provides a source parser for *.ipynb
files. Custom Sphinx directives are used to show Jupyter Notebook code cells
(and of course their results) in both HTML and LaTeX output. Unevaluated
notebooks, i.e. notebooks without stored output cells, will be automatically
executed during the Sphinx build process.

%if_with docs
%package -n python3-module-%oname-doc
Summary:        nbsphinx documentation
Group: Development/Documentation
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-doc
Documentation for nbsphinx
%endif
%endif

%prep
%setup
%patch0 -p1
%patch1 -p1
echo %version > version.txt

%if_with python3
cp -a . ../python3
%endif

%build
%python_build

#PYTHONPATH=. sphinx-build doc html
# remove the sphinx-build leftovers
#rm -rf html/{.doctrees,.buildinfo,conf.py}

%if_with python3
pushd ../python3
%python3_build

%if_with docs
PYTHONPATH=. py3_sphinx-build doc html
# remove the sphinx-build leftovers
rm -rf html/{.doctrees,.buildinfo,conf.py}
%endif
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc LICENSE README.rst
%python_sitelibdir/%oname.py*
%python_sitelibdir/%oname-%version-py2*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.rst
%python3_sitelibdir/__pycache__/%{oname}*
%python3_sitelibdir/%{oname}.py*
%python3_sitelibdir/%oname-%version-py3*.egg-info

%if_with docs
%files -n python3-module-%oname-doc
%doc LICENSE html
%endif
%endif

%changelog
* Tue Nov 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.15-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Miro Hrončok <mhroncok@redhat.com> - 0.2.13-1
- Initial package
