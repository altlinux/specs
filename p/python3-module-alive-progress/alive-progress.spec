%define _unpackaged_files_terminate_build 1
%def_with check
%define pypi_name alive-progress
%define mod_name alive_progress

Name: python3-module-%pypi_name
Version: 3.1.5
Release: alt1

Summary: A new kind of Progress Bar
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/alive-progress/
Vcs: https://github.com/rsalmei/alive-progress

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-about-time
BuildRequires: python3-module-click
BuildRequires: python3-module-grapheme
%endif

# AutoReq can't find dependency due to nested import
Requires: python3-module-grapheme

%description
Have you ever wondered where your lengthy processing was at,
and when would it finish?
Do you usually hit RETURN several times to make sure it didn't crash,
or the SSH connection didn't freeze?
Have you ever thought it'd be awesome to be able to pause some
processing without hassle, return to the Python prompt to manually fix
some items, then seamlessly resume it? I did...

I've started this new progress bar thinking about all that,
behold the alive-progress!

%prep
%setup -q

%build
%pyproject_build

%install
%pyproject_install
# Remove wrongly installed LICENSE
rm %buildroot/%_usr/LICENSE

%check
%pyproject_run_pytest

%files
%doc README.md CHANGELOG.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Wed Dec 20 2023 Alexander Kuznetsov <kuznetsovam@altlinux.org> 3.1.5-alt1
- Initial build.
