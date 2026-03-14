%define _unpackaged_files_terminate_build 1
%define pypi_name signxml
%define mod_name signxml

%def_with check

Name: python3-module-%pypi_name
Version: 4.4.0
Release: alt1

Summary: Python XML Signature and XAdES library
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/signxml/
Vcs: https://github.com/XML-Security/signxml

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
SignXML is an implementation of the W3C XML Signature standard in
Python. This standard (also known as "XMLDSig") is used to provide
payload security in SAML 2.0, XAdES, EBICS, and WS-Security, among
other uses. The standard is defined in the W3C Recommendation XML
Signature Syntax and Processing Version 1.1. SignXML implements all
of the required components of the Version 1.1 standard, and most
recommended ones.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python3 ./test/test.py -v

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Mar 14 2026 Anton Zhukharev <ancieg@altlinux.org> 4.4.0-alt1
- Updated to 4.4.0.

* Fri Jan 23 2026 Anton Zhukharev <ancieg@altlinux.org> 4.2.2-alt1
- Packaged for ALT Sisyphus.
