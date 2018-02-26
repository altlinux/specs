%define		php5_extension	fileinfo

Name:	 	php5-%php5_extension
Version:	%php5_version
Release:	%php5_release
Group:		System/Servers
License:	PHP Licence

Serial:		1

BuildRequires(pre): rpm-build-php5
BuildPreReq: php5-devel = %php5_version

# Automatically added by buildreq on Wed Mar 03 2010
BuildRequires: libmagic-devel

Summary:	Fileinfo extension try to guess the content type and encoding of a file

Source1:	php5-%php5_extension.ini
Source2:	php5-%php5_extension-params.sh

%description 
The functions in this module try to guess the content type and encoding
of a file by looking for certain magic byte sequences at specific
positions within the file. While this is not a bullet proof approach
the heuristics used do a very good job.

Additionally it can also be used to retrieve the mime type
for a particular file and for text files proper language encoding.

%prep
%setup -T -c
cp -pr %php5_extsrcdir/%php5_extension/* .

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-%php5_extension=%_usr
%php5_make

%install
%php5_make_install
install -D -m 644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%doc CREDITS

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 1:5.3.10.20120202-alt1
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 1:5.3.8.20110823-alt1
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 1:5.3.6.20110317-alt1
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 1:5.3.5.20110105-alt2
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 1:5.3.5.20110105-alt1
- Rebuild with php5-5.3.5.20110105-alt1

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 1:5.3.3.20100722-alt3
- Rebuild with php5-5.3.3.20100722-alt3

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 1:5.3.3.20100722-alt2
- Rebuild with php5-5.3.3.20100722-alt2

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 1:5.3.3.20100722-alt1
- Rebuild with php5-5.3.3.20100722-alt1

* Thu Aug 05 2010 Anton Farygin <rider@altlinux.ru> 1:1.0.4-alt10
- Rebuild with php5-5.2.14.20100721-alt1

* Wed Mar 10 2010 Anton Farygin <rider@altlinux.ru> 1:1.0.4-alt9
- Rebuild with php5-5.2.13.20100205-alt1

* Wed Mar  3 2010 Sergey Kurakin <kurakin@altlinux.org> 1:1.0.4-alt8
- Rebuild with php5-5.2.12.20091216-alt5
- Summary and description updated
- Minor spec cleanup

* Thu Jul 23 2009 Alexey Gladkov <legion@altlinux.ru> 1:1.0.4-alt7
- Rebuild with new php (5.2.11.20090722).

* Fri Feb 06 2009 Alexey Gladkov <legion@altlinux.ru> 1:1.0.4-alt6
- Rebuild with new php snapshot.

* Tue Sep 23 2008 Alexey Gladkov <legion@altlinux.ru> 1:1.0.4-alt5
- Rebuild with new php snapshot.

* Thu Jul 03 2008 Alexey Gladkov <legion@altlinux.ru> 1:1.0.4-alt4
- rebuild with new php5 (5.2.7).

* Sun Mar 30 2008 L.A. Kostis <lakostis@altlinux.ru> 1:1.0.4-alt3
- rebuild with new php5 (5.2.5).

* Sun Jun 03 2007 L.A. Kostis <lakostis@altlinux.ru> 1:1.0.4-alt2
- rebuild with new php5 (5.2.3).

* Thu May 31 2007 L.A. Kostis <lakostis@altlinux.ru> 1:1.0.4-alt1.2
- remove unnecessary requires.

* Sun May 20 2007 L.A. Kostis <lakostis@altlinux.ru> 1:1.0.4-alt1.1
- fix a typo in .ini.

* Sun May 13 2007 L.A. Kostis <lakostis@altlinux.ru> 1:1.0.4-alt1
- first build for Sisyphus.


