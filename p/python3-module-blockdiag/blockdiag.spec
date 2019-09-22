%define srcname blockdiag

Name:    python3-module-%srcname
Version: 1.5.4
Release: alt1

Summary: Generate block-diagram images from text

License: ASL 2.0
Group: Development/Python3
Url: http://blockdiag.com/

Source: %srcname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev

%description
blockdiag and its family generate diagram images from simply text file.

Features:
- Generates beautiful diagram images from simple text format (similar to
  graphviz's DOT format)
- Layouts diagram elements automatically
- Embeds to many documentations; Sphinx, Trac, Redmine and some wikis

- Supports many types of diagrams
  - block diagram (with this package)
  - sequence diagram (with the seqdiag package)
  - activity diagram (with the actdiag package)
  - logical network diagram (with the nwdiag package)

Enjoy documentation with blockdiag !

%prep
%setup -n %srcname-%version

%build
%python3_build

%install
%python3_install
%if "3"=="3"
mv %buildroot%_bindir/blockdiag %buildroot%_bindir/blockdiag3
%endif


%files
%_bindir/blockdiag3
%python3_sitelibdir/%{srcname}*

%changelog
* Mon Sep 23 2019 Grigory Ustinov <grenka@altlinux.org> 1.5.4-alt1
- Initial build for Sisyphus.
