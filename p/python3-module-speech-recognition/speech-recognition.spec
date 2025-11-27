%define _unpackaged_files_terminate_build 1
%define pypi_name speech-recognition
%define module_name speech_recognition
%define mod_name speechrecognition

%def_with check

Name: python3-module-%pypi_name
Version: 3.14.4
Release: alt1
Summary: Speech recognition module for Python, supporting several engines and APIs, online and offline.
License: BSD-3-Clause and GPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/SpeechRecognition/
Vcs: https://github.com/Uberi/speech_recognition
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-standard-aifc
BuildRequires: python3-module-audioop-lts
BuildRequires: flac
BuildRequires: python3(httpx)
BuildRequires: python3(numpy)
BuildRequires: python3(respx)

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%package -n python3-module-%pypi_name-tests
Summary: tests for %pypi_name
Group: Development/Python3

%description -n python3-module-%pypi_name-tests
This package contains tests for %pypi_name

%description
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%python3_sitelibdir/%module_name/flac-linux-x86 \
%buildroot%python3_sitelibdir/%module_name/flac-linux-x86_64 \
%buildroot%python3_sitelibdir/%module_name/flac-mac \
%buildroot%python3_sitelibdir/%module_name/flac-win32.exe || true
mkdir -p %buildroot%python3_sitelibdir/%pypi_name/tests
mv %buildroot%python3_sitelibdir/tests %buildroot%python3_sitelibdir/%pypi_name/

%check
#no audio during build
#pyproject_run_pytest 

%files
%doc MANIFEST.in README.rst LICENSE.txt LICENSE-FLAC.txt
%_bindir/sprc
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%files -n python3-module-%pypi_name-tests
%python3_sitelibdir/%pypi_name/tests/

%changelog
* Thu Nov 27 2025 Pavel Shilov <zerospirit@altlinux.org> 3.14.4-alt1
- Initial build for Sisyphus.
