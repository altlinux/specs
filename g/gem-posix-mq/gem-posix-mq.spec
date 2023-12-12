%define        _unpackaged_files_terminate_build 1
%define        gemname posix_mq

Name:          gem-posix-mq
Version:       2.4.1
Release:       alt4
Summary:       POSIX Message Queues for Ruby
License:       GPL-2.0 or LGPL-3.0+
Group:         Development/Ruby
Url:           https://yhbt.net/ruby_posix_mq.git/
Vcs:           https://yhbt.net/ruby_posix_mq.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(posix_mq) = 2.4.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names posix_mq,posix-mq
Obsoletes:     ruby-posix_mq
Provides:      ruby-posix_mq
Provides:      gem(posix_mq) = 2.4.1

%ruby_bindir_to %ruby_bindir

%description
POSIX message queues allow local processes to exchange data in the form of
messages. This API is distinct from that provided by System V message queues,
but provides similar functionality.


%package       -n posix-mq-rb
Version:       2.4.1
Release:       alt4
Summary:       POSIX Message Queues for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета posix_mq
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(posix_mq) = 2.4.1

%description   -n posix-mq-rb
POSIX Message Queues for Ruby executable(s).

POSIX message queues allow local processes to exchange data in the form of
messages. This API is distinct from that provided by System V message queues,
but provides similar functionality.

%description   -n posix-mq-rb -l ru_RU.UTF-8
Исполнямка для самоцвета posix_mq.


%package       -n gem-posix-mq-doc
Version:       2.4.1
Release:       alt4
Summary:       POSIX Message Queues for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета posix_mq
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(posix_mq) = 2.4.1

%description   -n gem-posix-mq-doc
POSIX Message Queues for Ruby documentation files.

POSIX message queues allow local processes to exchange data in the form of
messages. This API is distinct from that provided by System V message queues,
but provides similar functionality.

%description   -n gem-posix-mq-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета posix_mq.


%package       -n gem-posix-mq-devel
Version:       2.4.1
Release:       alt4
Summary:       POSIX Message Queues for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета posix_mq
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(posix_mq) = 2.4.1

%description   -n gem-posix-mq-devel
POSIX Message Queues for Ruby development package.

POSIX message queues allow local processes to exchange data in the form of
messages. This API is distinct from that provided by System V message queues,
but provides similar functionality.

%description   -n gem-posix-mq-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета posix_mq.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n posix-mq-rb
%doc README
%ruby_bindir/posix-mq-rb

%files         -n gem-posix-mq-doc
%doc README
%ruby_gemdocdir

%files         -n gem-posix-mq-devel
%doc README


%changelog
* Wed Dec 06 2023 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt4
- ! fixed spec format
- ! fixed git repo url

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt3
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt2
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1.1
- Rebuild with Ruby 2.5.0

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
