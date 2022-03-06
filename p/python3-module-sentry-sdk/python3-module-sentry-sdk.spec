%define oname sentry-sdk
%define sourcename sentry-python

Name: python3-module-%oname
Version: 1.5.4
Release: alt1
Summary: Sentry SDK for Python 3
License: BSD-2-Clause
Group: Development/Python3
Url: https://github.com/getsentry/sentry-python
# Source-url: %url/releases/download/%version/%oname-%version.tar.gz
Source: %sourcename-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
Bad software is everywhere, and we're tired of it.
Sentry is on a mission to help developers write
better software faster, so we can get back to
enjoying technology.
This is the next line of the Python SDK for Sentry,
intended to replace the raven package on PyPI.

%prep
%setup -n %sourcename-%version

# drop chalice integration
rm -r sentry_sdk/integrations/chalice.py

# drop old egg-info
rm -r sentry_sdk.egg-info

%build
%python3_build

%install
%python3_install

%files -n python3-module-%oname
%doc README.md
%python3_sitelibdir/*

%changelog
* Wed Jan 26 2022 Anton Midyukov <antohami@altlinux.org> 1.5.4-alt1
- initial build
