# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

#%%def_disable check

%define modulename immutabledict

Name: python3-module-%modulename
Version: 2.2.4
Release: alt1
Summary: A fork of frozendict, an immutable wrapper around dictionaries

License: MIT
Group: Development/Python3
Url: https://github.com/corenting/immutabledict

# Source-url: https://files.pythonhosted.org/packages/source/i/immutabledict/immutabledict-%version.tar.gz
Source: %modulename-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(poetry)
BuildRequires: python3(poetry.core)

%if_disabled check
%else
BuildRequires: pytest3
%endif

%description
It implements the complete mapping interface and can be used as a drop-in
replacement for dictionaries where immutability is desired. The immutabledict
constructor mimics dict, and all of the expected interfaces (iter, len, repr,
hash, getitem) are provided. Note that an immutabledict does not guarantee
the immutability of its values, so the utility of hash method is restricted
by usage.

The only difference is that the copy() method of immutable takes variable
keyword arguments, which will be present as key/value pairs in the new,
immutable copy.

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install

%check
pytest3 -v

%files
%doc README.md
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Thu Jun 15 2023 Anton Midyukov <antohami@altlinux.org> 2.2.4-alt1
- new version (2.2.4) with rpmgs script
- Migration to PEP517
- enable check

* Fri Feb 04 2022 Anton Midyukov <antohami@altlinux.org> 2.2.1-alt1
- initial build
