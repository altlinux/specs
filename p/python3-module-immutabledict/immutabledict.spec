%define modulename immutabledict

Name: python3-module-%modulename
Version: 2.2.1
Release: alt1
Summary: A fork of frozendict, an immutable wrapper around dictionaries

License: MIT
Group: Development/Python3
Url: https://github.com/corenting/immutabledict
# Source-url: https://files.pythonhosted.org/packages/source/i/immutabledict/immutabledict-%version.tar.gz

Source: %modulename-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

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
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Fri Feb 04 2022 Anton Midyukov <antohami@altlinux.org> 2.2.1-alt1
- initial build
