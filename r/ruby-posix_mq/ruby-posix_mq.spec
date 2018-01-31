%define pkgname ruby-posix_mq

Name: %pkgname
Version: 2.4.1
Release: alt1

Summary: POSIX Message Queues for Ruby.
Group: Development/Ruby
License: LGPL
Url: http://bogomips.org/ruby_posix_mq/

Source: %pkgname-%version.tar

BuildRequires: libruby-devel ruby-test-unit ruby-tool-setup

%description
POSIX message queues allow local processes to exchange data in the form
of messages. This API is distinct from that provided by System V
message queues, but provides similar functionality.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name.

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
* Wed Jan 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1
- New version.

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1.1
- Rebuild with Ruby 2.4.1

* Tue Mar 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- new version 2.3.0

* Wed Mar 19 2014 Led <led@altlinux.ru> 1.0.0-alt2.2
- Rebuilt with ruby-2.0.0-alt1

* Thu Dec 06 2012 Led <led@altlinux.ru> 1.0.0-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Aug 15 2011 Anton Gorlov <stalker@altlinux.ru> 1.0.0-alt2
- fix wrong url

* Thu Aug 11 2011 Anton Gorlov <stalker@altlinux.ru> 1.0.0-alt1
- initial build for ALTLinux
