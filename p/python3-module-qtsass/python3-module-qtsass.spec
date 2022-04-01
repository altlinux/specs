%define _unpackaged_files_terminate_build 1
%define pypi_name qtsass

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt2

License: MIT
Group: Development/Python
Url: https://github.com/spyder-ide/qtsass

Summary: QtSASS: Compile SCSS files to Qt stylesheets

# Source-url: https://github.com/spyder-ide/qtsass/archive/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar
Patch0: qtsass-0.3.0-Add-check-for-deprecated-api-between-2-and-3-version.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(sass)

BuildRequires: python3(pytest)

BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
SASS brings countless amazing features to CSS.
Besides being used in web development,
CSS is also the way to stylize Qt-based desktop applications.
However, Qt's CSS has a few variations that prevent the direct use of SASS compiler.

The purpose of this tool is to fill the gap between SASS and Qt-CSS by handling those variations.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    {envbindir}/pytest -vra {posargs:tests}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr --develop

%files
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-py%_python3_version.egg-info/

%changelog
* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 0.3.0-alt2
- Fixed FTBFS (Python 3.10).

* Thu Mar 19 2020 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- new version 0.3.0 (with rpmrb script)

* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1.git132651a
- initial build for ALT Sisyphus
