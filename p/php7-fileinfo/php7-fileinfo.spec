%define		php7_extension	fileinfo

Name:	 	php7-%php7_extension
Version:	%php7_version
Release:	%php7_release
Group:		System/Servers
License:	PHP Licence

Epoch:		1

BuildRequires(pre): rpm-build-php7
BuildPreReq: php7-devel = %php7_version

# Automatically added by buildreq on Wed Mar 03 2010
BuildRequires: libmagic-devel

Summary:	Fileinfo PHP extension try to guess the content type and encoding of a file

Source1:	php-%php7_extension.ini
Source2:	php-%php7_extension-params.sh

%description 
The functions in this module try to guess the content type and encoding
of a file by looking for certain magic byte sequences at specific
positions within the file. While this is not a bullet proof approach
the heuristics used do a very good job.

Additionally it can also be used to retrieve the mime type
for a particular file and for text files proper language encoding.

%prep
%setup -T -c
cp -pr %php7_extsrcdir/%php7_extension/* .

%build
phpize

BUILD_HAVE=`echo %php7_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php7_version
%configure \
	--with-%php7_extension=%_usr
%php7_make

%install
%php7_make_install
install -D -m 644 %SOURCE1 %buildroot/%php7_extconf/%php7_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php7_extconf/%php7_extension/params

%files
%php7_extconf/%php7_extension
%php7_extdir/*
%doc CREDITS

%post
%php7_extension_postin

%preun
%php7_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} 1:%version-%release
- Rebuild with php7-%version-%release
