%def_with check
Name: python3-module-sphinx-automodapi
Version: 0.14.1
Release: alt1
License: MIT
Source: sphinx-automodapi-%version.tar.gz
Group: Development/Python3
BuildArch: noarch
Summary: A sphinx extension to automatically generate API pages for whole modules

# Automatically added by buildreq on Mon Apr 25 2022
# optimized out: ca-trust fontconfig git-core glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error mercurial mpdecimal python3 python3-base python3-dev python3-module-Pygments python3-module-alabaster python3-module-apipkg python3-module-attrs python3-module-babel python3-module-charset-normalizer python3-module-docutils python3-module-filelock python3-module-idna python3-module-imagesize python3-module-iniconfig python3-module-jinja2 python3-module-markupsafe python3-module-packaging python3-module-pep517 python3-module-pkg_resources python3-module-platformdirs python3-module-pluggy python3-module-py python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-requests python3-module-setuptools python3-module-six python3-module-sphinx python3-module-system-seed-wheels python3-module-tomli python3-module-urllib3 sh4 xz
BuildRequires: python3-module-build python3-module-flit python3-module-setuptools_scm python3-module-wheel python3-module-sphinx_rtd_theme

%if_with check
BuildRequires: graphviz python3-module-Cython python3-module-build python3-module-flit python3-module-setuptools_scm python3-module-sphinxcontrib-applehelp python3-module-sphinxcontrib-devhelp python3-module-sphinxcontrib-htmlhelp python3-module-sphinxcontrib-qthelp python3-module-sphinxcontrib-serializinghtml python3-module-virtualenv python3-module-wheel
%endif

%description
This is a Sphinx extension to automatically generate API pages for whole
modules. It was originally developed for the Astropy project but is now
available as a standalone package since it can be used for any other
package. The documentation can be found on
http://sphinx-automodapi.readthedocs.io/en/latest/

%prep
%setup -n sphinx-automodapi-%version
for N in $(grep -rl "python': ('https://docs.python.org/" sphinx_automodapi/tests); do
        sed -i "s@'https://docs.python.org/{0}/'.format(sys.version_info.0.)@'/usr/share/python-sphinx/'@" "$N"
done

%build
python3 -m build -w -n
PYTHONPATH=`pwd` make -C docs SPHINXBUILD=sphinx-build-3 html

%install
pip3 install --no-deps --root=%buildroot -I dist/sphinx_automodapi*%{version}*.whl

%if_with check
python3 -m pytest --pyargs sphinx_automodapi -Wignore
%endif

%files
%doc docs/_build/html *.rst
%python3_sitelibdir_noarch/*

%changelog
* Mon Apr 25 2022 Fr. Br. George <george@altlinux.org> 0.14.1-alt1
- Autobuild version bump to 0.14.1

* Mon Apr 25 2022 Fr. Br. George <george@altlinux.ru> 0.14.10-alt1
- Initial build for ALT
