%define        gemname xmlrpc

Name:          gem-xmlrpc
Version:       0.3.2
Release:       alt1
Summary:       The Ruby standard library package 'xmlrpc'
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/xmlrpc
Vcs:           https://github.com/ruby/xmlrpc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(webrick) >= 0
Obsoletes:     ruby-xmlrpc < %EVR
Provides:      ruby-xmlrpc = %EVR
Provides:      gem(xmlrpc) = 0.3.2


%description
XMLRPC is a lightweight protocol that enables remote procedure calls over HTTP.
It is defined at http://www.xmlrpc.com.

XMLRPC allows you to create simple distributed computing solutions that span
computer languages. Its distinctive feature is its simplicity compared to other
approaches like SOAP and CORBA.

The Ruby standard library package 'xmlrpc' enables you to create a server that
implements remote procedures and a client that calls them. Very little code is
required to achieve either of these.


%package       -n gem-xmlrpc-doc
Version:       0.3.2
Release:       alt1
Summary:       The Ruby standard library package 'xmlrpc' documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета xmlrpc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(xmlrpc) = 0.3.2

%description   -n gem-xmlrpc-doc
The Ruby standard library package 'xmlrpc' documentation files.

XMLRPC is a lightweight protocol that enables remote procedure calls over HTTP.
It is defined at http://www.xmlrpc.com.

XMLRPC allows you to create simple distributed computing solutions that span
computer languages. Its distinctive feature is its simplicity compared to other
approaches like SOAP and CORBA.

The Ruby standard library package 'xmlrpc' enables you to create a server that
implements remote procedures and a client that calls them. Very little code is
required to achieve either of these.

%description   -n gem-xmlrpc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета xmlrpc.


%package       -n gem-xmlrpc-devel
Version:       0.3.2
Release:       alt1
Summary:       The Ruby standard library package 'xmlrpc' development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета xmlrpc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(xmlrpc) = 0.3.2
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-xmlrpc-devel
The Ruby standard library package 'xmlrpc' development package.

XMLRPC is a lightweight protocol that enables remote procedure calls over HTTP.
It is defined at http://www.xmlrpc.com.

XMLRPC allows you to create simple distributed computing solutions that span
computer languages. Its distinctive feature is its simplicity compared to other
approaches like SOAP and CORBA.

The Ruby standard library package 'xmlrpc' enables you to create a server that
implements remote procedures and a client that calls them. Very little code is
required to achieve either of these.

%description   -n gem-xmlrpc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета xmlrpc.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-xmlrpc-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-xmlrpc-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.2-alt1
- ^ 0.3.0 -> 0.3.2

* Mon Jan 14 2019 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus, packaged as a gem
