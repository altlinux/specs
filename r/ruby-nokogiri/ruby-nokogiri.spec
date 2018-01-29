%define Name Nokogiri
%define bname nokogiri
Name: ruby-%bname
Version: 1.8.2
Release: alt1
Summary: Ruby libraries for %Name (HTML, XML, SAX, and Reader parser)
Group: Development/Ruby
License: MIT/Ruby
URL: http://%bname.org
Source: %bname-%version.tar

BuildPreReq: rpm-build-ruby
BuildRequires: ruby ruby-stdlibs libruby-devel ruby-racc ruby-tool-setup %_bindir/rexical
BuildRequires: libxml2-devel libxslt-devel java-devel ruby-pkg-config
#BuildRequires: db2latex-xsl xhtml1-dtds

%filter_from_requires /^ruby(.*\.jar)/d

%description
%Name parses and searches XML/HTML very quickly, and also has correctly
implemented CSS3 selector support as well as XPath support.
This package contanis Ruby libraries for Nokogiri.


%package -n %bname
Summary: HTML, XML, SAX, and Reader parser
Group: Development/Other
BuildArch: noarch
Requires: ruby >= 1.8
Requires: %name = %version-%release

%description -n %bname
%Name parses and searches XML/HTML very quickly, and also has correctly
implemented CSS3 selector support as well as XPath support.
This package contanis Ruby libraries for Nokogiri.


%package doc
Summary: Documentation for %Name
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation for %Name.


%prep
%setup -q -n %bname-%version

DisableTest()
{
	local f="$1"

	shift
	while [ -n "$1" ]; do
		sed -i -r \
			-e "/^[[:blank:]]*def[[:blank:]]+test_$1[[:blank:]]*$/iif false" \
			-e "/^[[:blank:]]*def[[:blank:]]+test_$1[[:blank:]]*$/,/^[[:blank:]]*$/s/^[[:blank:]]*$/end\n&/" \
			"test/$f.rb"
		shift
	done
}

DisableTest test_convert_xpath multiple_filters
DisableTest css/test_nthiness last_of_type nth_last_of_type nth_of_type

%update_setup_rb


%build
%ruby_config -- --use-system-libraries
%ruby_build


%install
%ruby_install
%rdoc lib/
ls -d %buildroot%ruby_ri_sitedir/* | grep -v '/%Name$' | xargs rm -rf

%check
%ruby_test_unit -Ilib:ext:test test

%files
%ruby_sitelibdir/%bname
%ruby_sitelibdir/xsd
%ruby_sitelibdir/*.jar
%ruby_sitelibdir/*.rb
%ruby_sitearchdir/*


%files -n %bname
%_bindir/*


%files doc
%ruby_ri_sitedir/*


%changelog
* Mon Jan 29 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.2-alt1
- New version.

* Wed Sep 20 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.1-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1.1
- Rebuild with Ruby 2.4.1

* Mon Jun 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- New version

* Wed May 10 2017 Andrey Cherepanov <cas@altlinux.org> 1.7.2-alt1
- New version

* Mon Mar 20 2017 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- Nrw version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.7.0.1-alt1
- New version
- Rebuild with new %%ruby_sitearchdir location

* Mon Sep 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.6.8-alt1
- New version

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 1.6.6.2-alt1
- 1.6.6.2
- Rebuild with new version of libxml2

* Wed Mar 19 2014 Led <led@altlinux.ru> 1.6.1-alt2
- Rebuilt with ruby-2.0.0-alt1

* Sat Mar 15 2014 Led <led@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Fri Apr 12 2013 Led <led@altlinux.ru> 1.5.9-alt1
- 1.5.9
- updated URL
- updated BuildRequires
- fixed Group for %%name-doc subpackage
- moved %%_bindir/nokogiri to separate subpackage

* Sat Dec 15 2012 Led <led@altlinux.ru> 1.5.5-alt2
- fixed for renamed %_bindir/rex -> %_bindir/rexical
- %%files: fixed "File listed twice"

* Fri Dec 07 2012 Led <led@altlinux.ru> 1.5.5-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Mar 24 2012 Andriy Stepanov <stanv@altlinux.ru> 1.5.5-alt1
- New version

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.4.4.2-alt2
- Fix build

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.4.4.2-alt1
- [1.4.4.2]

* Wed Mar 17 2010 Timur Batyrshin <erthad@altlinux.org> 1.4.0-alt1
- [1.4.0]

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.3.2-alt1
- [1.3.2]

* Thu Sep 25 2008 Grigory Batalov <bga@altlinux.ru> 1.1.0-alt1
- Initial build for ALT Linux.
