# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/bison /usr/bin/docbook-to-man /usr/bin/docbook2html /usr/bin/doxygen /usr/bin/gtkdocize /usr/bin/guile /usr/bin/guile-config /usr/bin/indent /usr/bin/pkg-config /usr/bin/swig /usr/bin/valgrind cppunit-devel gcc-c++ gcc-fortran glib2-devel guile18-devel imlib2-devel libGL-devel libX11-devel libXext-devel libaccounts-glib-devel libexpat-devel libflac-devel libfreetype-devel libglibmm-devel libgmp-devel libhocr-devel libmpfr-devel liboggz-devel libreadline-devel libspeex-devel libuuid-devel libvorbis-devel pkgconfig(dbus-1) pkgconfig(freetype2) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) unzip zlib-devel
# END SourceDeps(oneline)
BuildRequires: chrpath
%add_optflags %optflags_shared
%define version 0.10.17
%define name libhocr
# Override default upstream location [/usr/share/doc/libhocr]
%define	hocrdocdir	%{_docdir}/%{name}-%{version}

# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:		libhocr
Version:	0.10.17
Release:	alt2_10
Summary:	A Hebrew optical character recognition library

Group:		System/Libraries
License:	GPLv3+
URL:		http://hocr.berlios.de
Source0:	http://download.berlios.de/hocr/%{name}-%{version}.tar.bz2
# Sent upstream (private mail, the project has no mailing list)
Patch0:		libhocr-missing-incl.patch
# Fix fedora bugs #574259, #577657, #574631
# Sent upstream (private mail, the project has no mailing list)
Patch1:		libhocr-no-scanner.patch

BuildRequires:	libfftw3-devel libhspell-devel libtiffxx-devel libtiff-devel
BuildRequires:	desktop-file-utils
BuildRequires:	swig python-devel libgtk+2-devel gettext
Source44: import.info

%description
LibHocr is a GNU Hebrew optical character recognition library. It scans
document images, improve the image, analyzes the page layout, recognizes
the characters and outputs the text. The output texts are now editable
text, ready for your blog, word processor or any other use.


%package        devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
# We ship *.pc files (requires the -devel of contained libs)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        gtk
Summary:	GTK+ application for %{name}
Group:		Text tools
Requires:	%{name} = %{version}-%{release}
Requires:	python-module-sane python-module-pygtk
Requires:	python(hocr) = %{version}-%{release}
# We use gtktextbuffer which uses gtkspell which have a runtime
# check of the spellcheck backends... so here it is:
Requires:	hspell

%description    gtk
The %{name}-gtk package contains a GUI application that uses %{name}.

%package        -n python-module-libhocr
Summary:	Python bindings for %{name}
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	python(hocr) = %{version}-%{release}

%description    -n python-module-libhocr
The %{name}-python package contains python binding for %{name}.


%prep
%setup -q
%patch0
%patch1


%build
export CFLAGS="%optflags -Werror-implicit-function-declaration"
%configure #--disable-static
make # %{?_smp_mflags}

find . -name '*.desktop' | while read file; do
	/usr/bin/desktop-file-validate "$file"
done


%install

# We must preserve timestamps so we don't cause
# problems for multilib architectures. Use install -p
# Ref: https://fedoraproject.org/wiki/PackagingDrafts/MultilibTricks#Timestamps
make install	\
	DESTDIR=%{buildroot}		\
	INSTALL="%{__install} -p"	\
	hocrdocdir=%{hocrdocdir}	\
	examples_binding_dir=%{hocrdocdir}/examples/bindings

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Remove static libs per Fedora packaging policy
find %{buildroot} -name '*.a' -exec rm -f {} ';'

rm -f %{buildroot}/%{hocrdocdir}/NEWS		# Empty, not usefull.
rm -f %{buildroot}/%{hocrdocdir}/INSTALL	# Not needed anymore ;-)

desktop-file-install --vendor="fedora"		\
	--add-category="Graphics"		\
	--delete-original			\
	--dir=%{buildroot}%{_datadir}/applications	\
	%{buildroot}/%{_datadir}/applications/hocr-gtk.desktop	\
	%{buildroot}/%{_datadir}/applications/sane-pygtk.desktop


%find_lang hocr-gtk
%find_lang sane-pygtk

cat hocr-gtk.lang sane-pygtk.lang > %{name}.lang
# kill rpath
for i in %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin}/*; do
	chrpath -d $i ||:
done
	    


%files
%doc %dir %{hocrdocdir}
%doc %{hocrdocdir}/AUTHORS
%doc %{hocrdocdir}/COPYING
%doc %{hocrdocdir}/ChangeLog
%doc %{hocrdocdir}/HACKING
%doc %{hocrdocdir}/README

%{_libdir}/*.so.*
%{_bindir}/hocr
%{_mandir}/man1/*.1*

%files devel
%doc %{_mandir}/man3/*.3*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{hocrdocdir}/examples

%files gtk -f %{name}.lang
%{_bindir}/hocr-gtk
%{_bindir}/sane-pygtk
%{_datadir}/applications/*.desktop
%{_datadir}/hocr-gtk
%{_datadir}/pixmaps/hocr1-128.png
%{_datadir}/pixmaps/hocr1-48.png
%{_datadir}/sane-pygtk

%files -n python-module-libhocr
# For noarch packages: sitelib
%{python_sitelib}/*.py*

# For arch-specific packages: sitearch
%{python_sitearch}/_hocr.so


%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_10
- update to new release by fcimport

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt2_9
- spec cleanup

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.10.17-alt1_9
- initial import by fcimport

