%define mname hachoir
%define oname %mname-core

%def_without python3

Name: python-module-%oname
Version: 1.3.3
Release: alt2.hg20120301
Epoch: 1

Summary: Core of Hachoir framework: parse and edit binary files
Group: Development/Python
License: GPLv2
Url: http://bitbucket.org/haypo/hachoir/wiki/hachoir-core
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/haypo/hachoir
Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-docutils
BuildPreReq: python-module-distribute python-module-PyQt4
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-docutils
BuildPreReq: python3-module-distribute python-tools-2to3
BuildPreReq: python3-module-PyQt4
%endif

%description
Hachoir is a Python library that allows to view and edit a binary stream
field by field. In other words, Hachoir allows you to "browse" any
binary stream just like you browse directories and files. A file is
split in a tree of fields, where the smallest field is just one bit.

%package -n python-module-%mname-metadata
Summary: Program to extract metadata using Hachoir library
Group: Development/Python
Requires: %name = %epoch:%version-%release
Requires: python-module-%mname-parser = %epoch:%version-%release

%description -n python-module-%mname-metadata
hachoir-metadata extracts metadata from multimedia files: music,
picture, video, but also archives. It supports most common file formats:

* Archives: bzip2, gzip, zip, tar
* Audio: MPEG audio ("MP3"), WAV, Sun/NeXT audio, Ogg/Vorbis (OGG),
  MIDI, AIFF, AIFC, Real audio (RA)
* Image: BMP, CUR, EMF, ICO, GIF, JPEG, PCX, PNG, TGA, TIFF, WMF, XCF
* Misc: Torrent
* Program: EXE
* Video: ASF format (WMV video), AVI, Matroska (MKV), Quicktime (MOV),
  Ogg/Theora, Real media (RM)

It tries to give as much information as possible. For some file formats,
it gives more information than libextractor for example, such as the
RIFF parser, which can extract creation date, software used to generate
the file, etc. But hachoir-metadata cannot guess informations. The most
complex operation is just to compute duration of a music using frame
size and file size.

%package -n python-module-%mname-metadata-qt
Summary: Qt4 interface of hachoir-metadata
Group: Development/Python
Requires: python-module-%mname-metadata = %epoch:%version-%release

%description -n python-module-%mname-metadata-qt
hachoir-metadata extracts metadata from multimedia files: music,
picture, video, but also archives. It supports most common file formats.

This package contains Qt4 interface of hachoir-metadata.

%package -n %mname-metadata-gtk
Summary: PyGTK interface of hachoir-metadata
Group: File tools
Requires: python-module-%mname-metadata = %epoch:%version-%release

%description -n %mname-metadata-gtk
hachoir-metadata extracts metadata from multimedia files: music,
picture, video, but also archives. It supports most common file formats.

This package contains PyGTK interface of hachoir-metadata.

%package -n python-module-%mname-parser
Summary: Package of Hachoir parsers used to open binary files
Group: Development/Python
Requires: %name = %epoch:%version-%release

%description -n python-module-%mname-parser
hachoir-parser is a package of most common file format parsers written
for Hachoir framework. Not all parsers are complete, some are very good
and other are poor: only parser first level of the tree for example.

A perfect parser have no "raw" field: with a perfect parser you are able
to know each bit meaning. Some good (but not perfect ;-)) parsers:

* Matroska video
* Microsoft RIFF (AVI video, WAV audio, CDA file)
* PNG picture
* TAR and ZIP archive

%package -n python-module-%mname-regex
Summary: Manipulation of regular expressions (regex)
Group: Development/Python

%description -n python-module-%mname-regex
hachoir-regex is a Python library for regular expression (regex or
regexp) manupulation. You can use a|b (or) and a+b (and) operators.
Expressions are optimized during the construction: merge ranges,
simplify repetitions, etc. It also contains a class for pattern matching
allowing to search multiple strings and regex at the same time.

%package -n python-module-%mname-subfile
Summary: Find subfile in any binary stream
Group: Development/Python

%description -n python-module-%mname-subfile
hachoir-subfile is a tool based on hachoir-parser to find subfiles in
any binary stream.

%package -n python-module-%mname-urwid
Summary: Binary file explorer using Hachoir and urwid libraries
Group: Development/Python

%description -n python-module-%mname-urwid
hachoir-urwid is a binary file explorer based on Hachoir library to
parse the files. Using this tool you can exactly know the meaning of
each bit/byte of your files. With direction keys, you can navigate in
the field tree. The key 'h' will disable 'human display' and switch to
'raw display'. It's sometime useful when you would like to compare
hexadecimal data and Hachoir reprensentation.

%if_with python3
%package -n python3-module-%oname
Summary: Core of Hachoir framework: parse and edit binary files (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Hachoir is a Python library that allows to view and edit a binary stream
field by field. In other words, Hachoir allows you to "browse" any
binary stream just like you browse directories and files. A file is
split in a tree of fields, where the smallest field is just one bit.

%package -n python3-module-%mname-metadata
Summary: Program to extract metadata using Hachoir library (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %epoch:%version-%release
Requires: python3-module-%mname-parser = %epoch:%version-%release

%description -n python3-module-%mname-metadata
hachoir-metadata extracts metadata from multimedia files: music,
picture, video, but also archives. It supports most common file formats:

* Archives: bzip2, gzip, zip, tar
* Audio: MPEG audio ("MP3"), WAV, Sun/NeXT audio, Ogg/Vorbis (OGG),
  MIDI, AIFF, AIFC, Real audio (RA)
* Image: BMP, CUR, EMF, ICO, GIF, JPEG, PCX, PNG, TGA, TIFF, WMF, XCF
* Misc: Torrent
* Program: EXE
* Video: ASF format (WMV video), AVI, Matroska (MKV), Quicktime (MOV),
  Ogg/Theora, Real media (RM)

It tries to give as much information as possible. For some file formats,
it gives more information than libextractor for example, such as the
RIFF parser, which can extract creation date, software used to generate
the file, etc. But hachoir-metadata cannot guess informations. The most
complex operation is just to compute duration of a music using frame
size and file size.

%package -n python3-module-%mname-metadata-qt
Summary: Qt4 interface of hachoir-metadata (Python 3)
Group: Development/Python3
Requires: python3-module-%mname-metadata = %epoch:%version-%release

%description -n python3-module-%mname-metadata-qt
hachoir-metadata extracts metadata from multimedia files: music,
picture, video, but also archives. It supports most common file formats.

This package contains Qt4 interface of hachoir-metadata.

%package -n python3-module-%mname-parser
Summary: Package of Hachoir parsers used to open binary files (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %epoch:%version-%release

%description -n python3-module-%mname-parser
hachoir-parser is a package of most common file format parsers written
for Hachoir framework. Not all parsers are complete, some are very good
and other are poor: only parser first level of the tree for example.

A perfect parser have no "raw" field: with a perfect parser you are able
to know each bit meaning. Some good (but not perfect ;-)) parsers:

* Matroska video
* Microsoft RIFF (AVI video, WAV audio, CDA file)
* PNG picture
* TAR and ZIP archive

%package -n python3-module-%mname-regex
Summary: Manipulation of regular expressions (regex) (Python 3)
Group: Development/Python3

%description -n python3-module-%mname-regex
hachoir-regex is a Python library for regular expression (regex or
regexp) manupulation. You can use a|b (or) and a+b (and) operators.
Expressions are optimized during the construction: merge ranges,
simplify repetitions, etc. It also contains a class for pattern matching
allowing to search multiple strings and regex at the same time.

%package -n python3-module-%mname-subfile
Summary: Find subfile in any binary stream (Python 3)
Group: Development/Python3

%description -n python3-module-%mname-subfile
hachoir-subfile is a tool based on hachoir-parser to find subfiles in
any binary stream.

%package -n python3-module-%mname-urwid
Summary: Binary file explorer using Hachoir and urwid libraries (Python 3)
Group: Development/Python3

%description -n python3-module-%mname-urwid
hachoir-urwid is a binary file explorer based on Hachoir library to
parse the files. Using this tool you can exactly know the meaning of
each bit/byte of your files. With direction keys, you can navigate in
the field tree. The key 'h' will disable 'human display' and switch to
'raw display'. It's sometime useful when you would like to compare
hexadecimal data and Hachoir reprensentation.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build --setuptools

pushd hachoir-metadata
%python_build --setuptools
popd

pushd hachoir-parser
ln -s README.header README
%python_build --setuptools
popd

pushd hachoir-regex
%python_build --setuptools
for i in regex regression; do
	rst2html.py $i.rst >$i.html
done
popd

pushd hachoir-subfile
%python_build --setuptools
popd

pushd hachoir-urwid
%python_build --setuptools
popd

%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build --setuptools

pushd hachoir-metadata
%python3_build --setuptools
popd

pushd hachoir-parser
ln -s README.header README
%python3_build --setuptools
popd

pushd hachoir-regex
%python3_build --setuptools
for i in regex regression; do
	rst2html.py $i.rst >$i.html
done
popd

pushd hachoir-subfile
%python3_build --setuptools
popd

pushd hachoir-urwid
%python3_build --setuptools
popd

popd
%endif

pushd doc
rst2html.py hachoir-api.rst >hachoir-api.html
rst2html.py internals.rst >internals.html
popd

%install
%if_with python3
pushd ../python3
%python3_install

pushd hachoir-metadata
%python3_install
popd

pushd hachoir-parser
%python3_install
popd

pushd hachoir-regex
%python3_install
popd

pushd hachoir-subfile
%python3_install
popd

pushd hachoir-urwid
%python3_install
popd

popd

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd
%endif

%python_install

pushd hachoir-metadata
%python_install
popd

pushd hachoir-parser
%python_install
popd

pushd hachoir-regex
%python_install
popd

pushd hachoir-subfile
%python_install
popd

pushd hachoir-urwid
%python_install
popd

%files
%doc AUTHORS COPYING ChangeLog README doc
%python_sitelibdir/hachoir_core*

%files -n python-module-%mname-metadata
%doc %mname-metadata/AUTHORS %mname-metadata/ChangeLog
%doc %mname-metadata/COPYING %mname-metadata/README
%_bindir/%mname-metadata
%python_sitelibdir/hachoir_metadata*
%exclude %python_sitelibdir/hachoir_metadata/qt

%files -n python-module-%mname-metadata-qt
%_bindir/%mname-metadata-qt
%python_sitelibdir/hachoir_metadata/qt

%files -n %mname-metadata-gtk
%_bindir/%mname-metadata-gtk

%files -n python-module-%mname-parser
%doc %mname-parser/AUTHORS %mname-parser/COPYING %mname-parser/ChangeLog
%doc %mname-parser/README* %mname-parser/tests
%python_sitelibdir/hachoir_parser*

%files -n python-module-%mname-regex
%doc %mname-regex/AUTHORS %mname-regex/COPYING %mname-regex/README
%doc %mname-regex/*.html
%python_sitelibdir/hachoir_regex*

%files -n python-module-%mname-subfile
%doc %mname-subfile/AUTHORS %mname-subfile/COPYING
%doc %mname-subfile/README
%_bindir/%mname-subfile
%python_sitelibdir/hachoir_subfile*

%files -n python-module-%mname-urwid
%doc %mname-urwid/AUTHORS %mname-urwid/COPYING %mname-urwid/README
%_bindir/%mname-urwid
%python_sitelibdir/hachoir_urwid*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS COPYING ChangeLog README doc
%python3_sitelibdir/hachoir_core*

%files -n python3-module-%mname-metadata
%doc %mname-metadata/AUTHORS %mname-metadata/ChangeLog
%doc %mname-metadata/COPYING %mname-metadata/README
%_bindir/%mname-metadata3
%python3_sitelibdir/hachoir_metadata*
%exclude %python3_sitelibdir/hachoir_metadata/qt

%files -n python3-module-%mname-metadata-qt
%_bindir/%mname-metadata-qt3
%python3_sitelibdir/hachoir_metadata/qt

%files -n python3-module-%mname-parser
%doc %mname-parser/AUTHORS %mname-parser/COPYING %mname-parser/ChangeLog
%doc %mname-parser/README* %mname-parser/tests
%python3_sitelibdir/hachoir_parser*

%files -n python3-module-%mname-regex
%doc %mname-regex/AUTHORS %mname-regex/COPYING %mname-regex/README
%doc %mname-regex/*.html
%python3_sitelibdir/hachoir_regex*

%files -n python3-module-%mname-subfile
%doc %mname-subfile/AUTHORS %mname-subfile/COPYING
%doc %mname-subfile/README
%_bindir/%mname-subfile3
%python3_sitelibdir/hachoir_subfile*

#files -n python3-module-%mname-urwid
#doc %mname-urwid/AUTHORS %mname-urwid/COPYING %mname-urwid/README
#_bindir/%mname-urwid3
#python3_sitelibdir/hachoir_urwid
%endif

%changelog
* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.3-alt2.hg20120301
- New snapshot

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.3-alt1.1
- Rebuild with Python-2.7

* Wed Aug 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.3-alt1
- Initial build for Sisyphus

