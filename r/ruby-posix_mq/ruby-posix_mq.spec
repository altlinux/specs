%define pkgname ruby-posix_mq

Name: %pkgname 
Version: 1.0.0
Release: alt2

Summary: POSIX Message Queues for Ruby.
Group: Development/Ruby 
License: LGPL
Url: http://bogomips.org/ruby_posix_mq/

Packager: Anton Gorlov <stalker at altlinux.org>

Source: %pkgname-%version.tar


# Automatically added by buildreq on Thu Aug 11 2011
# optimized out: ruby ruby-stdlibs ruby-tool-rdoc
BuildRequires: libruby-devel ruby-test-unit ruby-tool-setup

%description 
POSIX message queues allow local processes to exchange data in the form
of messages. This API is distinct from that provided by System V
message queues, but provides similar functionality.

%package doc 
Summary: Documentation files for %name 
Group: Documentation

%description doc 
Documentation files for %name

%prep
%setup -q -n %pkgname-%version 
%update_setup_rb

%build 
%ruby_config
%ruby_build
#for t in test/test_*.rb; do
#ruby_test_unit -Ilib/:ext/posix_mq  test/test_posix_mq.rb
#done



%install 
%ruby_install 
%rdoc lib/

%files 
%doc README
%_bindir/*
%ruby_sitearchdir/*
%ruby_sitelibdir/*

%files doc 
%doc LICENSE
%ruby_ri_sitedir/POSIX_MQ*

%changelog 
* Mon Aug 15 2011 Anton Gorlov <stalker@altlinux.ru> 1.0.0-alt2
- fix wrong url

* Thu Aug 11 2011 Anton Gorlov <stalker@altlinux.ru> 1.0.0-alt1
- initial build for ALTLinux




