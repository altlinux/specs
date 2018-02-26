Summary: Documentation for Festival
Name: festival-doc
Version: 1.4.2
Release: alt1
Packager: Igor Vlasenko <viy@altlinux.ru>
License: X11-like
Group: Sound
URL: http://www.cstr.ed.ac.uk/projects/speech_tools.html
Source0: festdoc-1.4.2.tar.gz
BuildArch: noarch

#BuildRequires: none

%description
Festival User Manual.
Authors - Alan W Black, Paul Taylor and Richard Caley.
This manual describes the Festival speech synthesis
 system from the user's point of view.

This package contains the pre-built HTML and Postscript versions of the
documentation for Festival.
 .
 Note that the info document for festival is included in the main
 festival package.



%package -n speech_tools-doc
Summary: Documentation for the Edinburgh Speech Tools
Group: Sound

%description -n speech_tools-doc
Edinburgh Speech Tools library documentation.
Authors - Alan W Black, Paul Taylor and Richard Caley.
This manual describes the executable programs which
accompany the Edinburgh Speech Tools library, as well as the C++ API
for the library itself.

This package contains the pre-built HTML and Postscript versions of the
 documentation for the Edinburgh Speech Tools.

%prep
%setup -q -n festdoc-%version

%build
## converted from debian rules makefile with debian2spec

# Upstream includes a few empty files
find . -type f -size 0 -print0 | xargs -0r rm

# Delete revision control files, if any
find . \( -name SCCS -o -name CVS -o -name RCS \) -print0 | xargs -0r rm -rf

rm festival/festival.ps
mv festival/html/festival*.ps.gz festival/

# removing logs
find speech_tools/doc -type f \( -name *_trace -or -name *_made  -or -name .*_made  -or -name .*_done -or -name Makefile -or -name make.include \) -print0 | xargs -0r rm

# removing sgml
find speech_tools/doc -type f \( -name *.sgml -or -name *.dtd  -or -name *.dsl -or -name INCLUDE_ONLY* \) -print0 | xargs -0r rm

# Delete empty dirs, if any
find speech_tools/doc -type d -size 0 -print0 | xargs -0r rmdir

mv speech_tools/doc speech_tools/html
 
%install
mkdir $RPM_BUILD_ROOT

#Document: festival
#Index: /usr/share/doc/festival-doc/festival/user-manual/festival_toc.html
#Document: speech-tools
#Index: /usr/share/doc/festival-doc/speechtools/index.html

%files 
%doc festival/html
%doc festival/festival*.ps*

%files -n speech_tools-doc
%doc speech_tools/html

%changelog
* Sat Oct 28 2006 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1
- first build for Sisyphus


