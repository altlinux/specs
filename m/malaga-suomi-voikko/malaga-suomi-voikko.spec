# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/col /usr/bin/compress /usr/bin/dvipdf /usr/bin/dvips /usr/bin/emacs /usr/bin/emacsclient /usr/bin/gconftool-2 /usr/bin/gdb /usr/bin/groff /usr/bin/gtar /usr/bin/gvim /usr/bin/gzip /usr/bin/ldd /usr/bin/less /usr/bin/lha /usr/bin/makeinfo /usr/bin/md5sum /usr/bin/perl /usr/bin/pg /usr/bin/pkg-config /usr/bin/runtest /usr/bin/shar /usr/bin/strip /usr/bin/texi2dvi /usr/bin/valgrind /usr/bin/xemacs /usr/bin/zip /usr/sbin/zdump bzlib-devel gcc-c++ gcc-fortran glib2-devel libICE-devel libSM-devel libX11-devel libao-devel libdbus-devel libexpat-devel libfuse-devel libgcrypt-devel libgmp-devel libncurses-devel libreadline-devel libtinfo-devel libxml2-devel pkgconfig(gconf-2.0) pkgconfig(gdk-pixbuf-xlib-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(libglade-2.0) pkgconfig(x11) python-devel unzip zlib-devel
# END SourceDeps(oneline)
Name:           malaga-suomi-voikko
Version:        1.10
Release:        alt1_2
Summary:        A description of Finnish morphology written in Malaga (Voikko edition)

Group:          Text tools
License:        GPLv2+
URL:            http://voikko.sourceforge.net/
# The usual format of stable release source URLs
Source0:        http://downloads.sourceforge.net/voikko/suomi-malaga-%{version}.tar.gz
# The usual format of testing release source URLs
#Source0:        http://www.puimula.org/htp/testing/suomi-malaga-%{version}rc3.tar.gz

BuildRequires:  malaga >= 7.8

# debuginfo would be empty
%define debug_package %{nil}
Source44: import.info

%description
A description of Finnish morphology written in Malaga. This package is built
to support the Voikko spellchecker/hyphenator, it doesn't support the Sukija
text indexer.

%prep
%setup -q -n suomi-malaga-%{version}


%build
# configure removed, not needed in this package
make %{?_smp_mflags} voikko


%install
# Files differ on big-endian and small-endian archs, and they have different
# names (*_l vs *_b). This is the reason we use %%{_libdir} instead of
# %%{_datadir} and won't noarch the package.
make voikko-install DESTDIR=$RPM_BUILD_ROOT%{_libdir}/voikko


%files
%doc ChangeLog CONTRIBUTORS COPYING README README.fi
%{_libdir}/voikko


%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_2
- update to new release by fcimport

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_1
- initial import by fcimport

