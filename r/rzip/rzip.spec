Name: rzip
Version: 2.1
Release: alt1
License: GPL
Summary: A large-file compression program 
Summary(ru_RU.CP1251): Программа для сжатия очень больших файлов
Group: Archiving/Compression
Source0: http://rzip.samba.org/ftp/rzip/%name-%version.tar.gz

URL: http://rzip.samba.org


BuildRequires: bzlib-devel

%description
rzip  is a file compression program designed to do particularly well on               
very large files containing long distance redundency.                                 

%description -l ru_RU.CP1251
rzip - это программа для сжатия, специально предназначенная для работы с
очень большими файлами, в следствие чего работает только с ними, не
поддерживая "трубы" (pipes) и прочее.

%prep
%setup -q 

%build
%configure 	--prefix=%_prefix

%make
%install

%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot%_man1dir

install -m 755 %name %buildroot%_bindir/
install -m 644 %name.1 %buildroot%_man1dir/


%files
%doc COPYING
%_bindir/rzip
%_man1dir/rzip.1.gz

%changelog
* Tue Oct 10 2006 Andrew Kornilov <hiddenman@altlinux.ru> 2.1-alt1
- New version
* Sun Jul 10 2005 Andrew Kornilov <hiddenman@altlinux.ru> 2.0-alt4
- Fixed permissions (#6015)

* Wed Aug 04 2004 Andrew Kornilov <hiddenman@altlinux.ru> 2.0-alt3
- Addes bzlib-devel to buildrequires

* Mon Mar 22 2004 Andrew Kornilov <hiddenman@altlinux.ru> 2.0-alt2
- Fixed few typos in spec, added spec translation to Russian

* Mon Mar 15 2004 Andrew Kornilov <andy@eva.dp.ua> 2.0-alt1
- First build for Sisyphus
