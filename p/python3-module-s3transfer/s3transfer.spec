%define _unpackaged_files_terminate_build 1
%define oname s3transfer

%def_with check

Name: python3-module-%oname
Version: 0.5.2
Release: alt1

Summary: An Amazon S3 Transfer Manager

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/s3transfer/

BuildArch: noarch

# Source-git: https://github.com/boto/s3transfer.git
Source: %name-%version.tar

Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(botocore)

# deps on packages bundled by botocore
BuildRequires: python3(requests)
BuildRequires: python3(six)

BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

# awscrt is extra stuff required by `s3transfer[crt]` => `botocore[crt]`
# awscrt is not packaged yet
%filter_from_requires /python3(awscrt\(\..*\)\?)/d

%description
%oname is a Python library for managing Amazon S3 transfers.

Note.
This project is not currently GA. If you are planning to use this code in
production, make sure to lock to a minor version as interfaces may break from
minor version to minor version.  For a basic, stable interface of %oname,
try the interfaces exposed in boto3.

%prep
%setup
%autopatch1 -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false --develop

%files
%doc *.rst
%doc LICENSE.txt
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info

%changelog
* Wed Mar 09 2022 Stanislav Levin <slev@altlinux.org> 0.5.2-alt1
- 0.3.3 -> 0.5.2.

* Thu Jun 17 2021 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt2
- build python3 module separately

* Tue Sep 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.3-alt1
- Updated to upstream version 0.3.3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.10-alt1
- Initial build for ALT.
