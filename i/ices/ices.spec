Name: ices
Version: 0.4
Release: alt6.1.1.1.1

Summary: Ices - sourcer for use with Icecast daemon.
Packager: Pavlov Konstantin <thresh@altlinux.ru>
License: GPL
Group: Sound
Url: http://www.icecast.org

Source: %name-%version.tar.gz
Patch0: ices-0.4-flac-1.1.3.patch

BuildPreReq: libshout2-devel >= 2.1-alt1

# Automatically added by buildreq on Sun Oct 16 2011
BuildRequires: gcc-c++ libfaad-devel libflac-devel liblame-devel libmpeg4ip-devel libshout2-devel libxml2-devel perl-devel python-devel

%description
Ices is a streamer for use with icecast.
This package includes full-featured version of ices, with perl
and python playlist handlers. Support FLAC, MP4, Vorbis and MP3 sources.

%prep
%setup -q -n %name-%version
%patch -p1

%build
%add_optflags "-I%_includedir/mpeg4"
%configure \
	--sysconfdir=%_sysconfdir/%name \
	--with-moddir=%_libdir/%name \
	--with-docdir=%_datadir/doc/%name-%version \
	--with-faad \
	--with-perl \
	--with-python
	
%make_build

%install

%make_install \
	DESTDIR=%buildroot \
	sysconfdir=%_sysconfdir/%name \
	moddir=%_libdir/%name \
	docdir=%_datadir/doc/%name-%version \
	install

find %buildroot{%_sysconfdir,%_libdir}/%name -type f -name '*.dist' |\
	sed 's|.dist$||' |xargs -iz mv -f z.dist z

%files
%doc AUTHORS BUGS COPYING INSTALL README*
%doc doc/icesmanual.html
%dir %_sysconfdir/%name
%dir %_libdir/%name
%config %_sysconfdir/%name/*
%_bindir/%name
%_libdir/%name/*
%_man1dir/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.4-alt6.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.4-alt6.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.4-alt6.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt6.1
- rebuild with new perl 5.20.1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 0.4-alt6
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 0.4-alt5
- rebuilt for perl-5.16

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt4.3.1
- Rebuild with Python-2.7

* Sun Oct 16 2011 Alexey Tourbin <at@altlinux.ru> 0.4-alt4.3
- rebuilt for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.4-alt4.2.1
- rebuilt with perl 5.12

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt4.2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.4-alt4.1
- Rebuilt with python-2.5.

* Sat Mar 03 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.4-alt4
- Added ices-0.4-flac-1.1.3.patch to build with new flac.
- Cleanup BuildRequires.
- Fixed description.
- Some spec cleanup.

* Fri Mar 25 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.4-alt3.2
- rebuild with mpeg4ip.

* Mon Mar 14 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.4-alt3.1
- rebuild with a new version of libshout2.

* Fri Mar 04 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.4-alt3
- Temporarily excluded mp4 support. Will add it when mpeg4ip package will be ready.

* Mon Nov 22 2004 Pavlov Konstantin <thresh@altlinux.ru> 0.4-alt2
- Rebuild with new libshout2.

* Wed Oct 20 2004 Pavlov Konstantin <thresh@altlinux.ru> 0.4-alt1
- Supports FLAC, MP4, Vorbis and MP3 sources.
- Initial build for ALT Linux Sisyphus.
