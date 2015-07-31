%define oname patool

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.8
Release: alt1.git20150719
Summary: Portable command line archive file manager
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/patool/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wummel/patool.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Various archive formats can be created, extracted, tested, listed,
searched, compared and repacked by patool. The advantage of patool is
its simplicity in handling archive files without having to remember a
myriad of programs and options.

The archive format is determined by the file(1) program and as a
fallback by the archive file extension.

patool supports 7z (.7z), ACE (.ace), ADF (.adf), ALZIP (.alz),
APE (.ape), AR (.a), ARC (.arc), ARJ (.arj), BZIP2 (.bz2), CAB (.cab),
COMPRESS (.Z), CPIO (.cpio), DEB (.deb), DMS (.dms), FLAC (.flac), GZIP
(.gz), ISO (.iso), LRZIP (.lrz), LZH (.lha, .lzh), LZIP (.lz), LZMA
(.lzma), LZOP (.lzo), RPM (.rpm), RAR (.rar), RZIP (.rz), SHN (.shn),
TAR (.tar), XZ (.xz), ZIP (.zip, .jar), ZOO (.zoo) and ZPAQ (.zpaq)
formats. It relies on helper applications to handle those archive
formats (for example bzip2 for BZIP2 archives).

The archive formats TAR, ZIP, BZIP2 and GZIP are supported natively and
do not require helper applications to be installed.

%if_with python3
%package -n python3-module-%oname
Summary: Portable command line archive file manager
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Various archive formats can be created, extracted, tested, listed,
searched, compared and repacked by patool. The advantage of patool is
its simplicity in handling archive files without having to remember a
myriad of programs and options.

The archive format is determined by the file(1) program and as a
fallback by the archive file extension.

patool supports 7z (.7z), ACE (.ace), ADF (.adf), ALZIP (.alz),
APE (.ape), AR (.a), ARC (.arc), ARJ (.arj), BZIP2 (.bz2), CAB (.cab),
COMPRESS (.Z), CPIO (.cpio), DEB (.deb), DMS (.dms), FLAC (.flac), GZIP
(.gz), ISO (.iso), LRZIP (.lrz), LZH (.lha, .lzh), LZIP (.lz), LZMA
(.lzma), LZOP (.lzo), RPM (.rpm), RAR (.rar), RZIP (.rz), SHN (.shn),
TAR (.tar), XZ (.xz), ZIP (.zip, .jar), ZOO (.zoo) and ZPAQ (.zpaq)
formats. It relies on helper applications to handle those archive
formats (for example bzip2 for BZIP2 archives).

The archive formats TAR, ZIP, BZIP2 and GZIP are supported natively and
do not require helper applications to be installed.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
rm -fR build
py.test -vv

%if_with python3
pushd ../python3
rm -fR build
py.test-%_python3_version -vv
popd
%endif

%files
%doc doc/*
%_bindir/*
%_man1dir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc doc/*
%_bindir/*.py3
%_man1dir/*
%python3_sitelibdir/*
%endif

%changelog
* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1.git20150719
- Initial build for Sisyphus

