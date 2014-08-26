%define oname fonttools
Name: python3-module-%oname
Version: 2.5
Release: alt1.git20140824

Summary: Converts OpenType and TrueType fonts to and from XML

Group: Development/Python3
License: LGPL
Url: http://sourceforge.net/projects/fonttools/

%add_python3_req_skip Res calldll macfs gtk

# https://github.com/behdad/fonttools.git
Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: xorg-sdk python3-module-numpy 

%description
TTX is a tool to convert OpenType and TrueType fonts to and from
XML. FontTools is a library for manipulating fonts, written in Python. It
supports TrueType, OpenType, AFM and to an extent Type 1 and some
Mac-specific formats.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%files
%_bindir/*
%python3_sitelibdir/*

%changelog
* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.git20140824
- Initial build for Sisyphus

