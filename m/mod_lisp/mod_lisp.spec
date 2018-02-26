Name:     mod_lisp
Version:  2.43
Release:  alt1

Summary:  mod_lisp is an Apache module to easily write web applications in Lisp
Group:    System/Servers
License:  BSD
Url:      http://www.fractalconcept.com/asp/mod_lisp
Packager: Alexey Voinov <voins@altlinux.ru>

Requires: apache

Source0:  mod_lisp.c
Source1:  mod_lisp.conf

# Automatically added by buildreq on Sun Nov 18 2007
BuildRequires: apache-devel

%description
mod_lisp talk from Apache to lisp processes by sockets with a very
straightforward protocol to handle a request. It now reuses the Apache
to Lisp sockets for improved performance. Future versions will
probably be more Lisp specific, but for now it can be used by any
other language.

%prep
mkdir -p %_builddir/%name-%version
cd %_builddir/%name-%version
cp %SOURCE0 .

%build
cd %_builddir/%name-%version
%apache_apxs -Wc,"$RPM_OPT_FLAGS" -o mod_lisp.so -c mod_lisp.c

%install
cd %_builddir/%name-%version
mkdir -p $RPM_BUILD_ROOT%_libdir/apache $RPM_BUILD_ROOT%apache_modconfdir
install -m644 mod_lisp.so $RPM_BUILD_ROOT%_libdir/apache/
install -m644 %SOURCE1 $RPM_BUILD_ROOT%apache_modconfdir

%post
%post_apacheconf

%postun
%postun_apacheconf

%files
%_libdir/apache/*
%config(noreplace) %apache_modconfdir/*

%changelog
* Sat Nov 17 2007 Alexey Voinov <voins@altlinux.ru> 2.43-alt1
- initial build for ALT Linux
