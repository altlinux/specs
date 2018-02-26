Name: mod_index_rss
Version: 1.0
Release: alt1

Summary: On-the-fly RSS output of directories
Group: System/Servers
License: BSD
Url: http://tangent.org

Source: http://download.tangent.org/mod_index_rss-%version.tar.gz
Source1: mod_index_rss.conf

%define apache_version 1.3.6
PreReq: apache >= %apache_version

%define apache_moduledir %(%apache_apxs -q LIBEXECDIR)

BuildPreReq: apache-devel >= %apache_version

# Automatically added by buildreq on Fri Sep 01 2006
BuildRequires: apache-devel

%description
%name is an Apache module that creates RSS of directory contents
on the fly. This can be used to publish static files (HTML, images,
etc.) to RSS feeds by placing them in a directory.

%prep
%setup -q

%build
make APXS=%apache_apxs

%install
install -d %buildroot{%apache_moduledir,%apache_modconfdir}
install -m755 mod_index_rss.so %buildroot%apache_moduledir
install -m644 %SOURCE1 %buildroot%apache_modconfdir

chmod -x faq.html

%post
/sbin/service httpd condrestart

%preun
/sbin/service httpd condrestart

%files
%apache_moduledir/*
%config(noreplace) %apache_modconfdir/mod_index_rss.conf
%doc faq.html

%changelog
* Fri Sep 01 2006 Victor Forsyuk <force@altlinux.ru> 1.0-alt1
- Initial build.
