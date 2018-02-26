Name: metalterator
Version: 1.2
Release: alt3

Source:%name-%version.tar.gz

Packager: Paul Wolneykien <manowar@altlinux.ru>

Summary: Alterator meta-backend with additional Guile modules
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Requires: alterator >= 4.8-alt1
Conflicts: alterator >= 5.0

# Automatically added by buildreq on Wed Apr 08 2009
BuildRequires: rpm-macros-alterator rpm-macros-fillup

%description
Alterator meta-backend uses a place on the filesystem as a persistent
store for object state. Each object represented as a *.scm file
containing an association list of object properties. Sub-objects are
placed in subdirectories.

Meta-backend can be accessed as a normal backend via Woo-bus and has
the base name "/meta". Filesystem place is determined by the remaining
part of the object name, i.e. "/meta/etc/metalterator/db1/obj1"
references a file /etc/metalterator/db1/obj1.scm.

The root object "/meta" properties are reserved for meta-backend itself
and represent meta-backend internal properties. To look inside an object
reading/writing process set property 'debug-level of the "/meta" backend
to a positive (1-5) value. Debugging messages can then be seen at the
`alteratord' console.

The (alterator metalterator) Guile module provides helpful procedures
for meta-backend communication.

%prep
%setup -q

%install
install -p -m0640 -D metalterator.scm %buildroot%_alterator_datadir/interfaces/guile/metalterator.scm
install -p -m0640 -D metalterator/match.scm %buildroot%_alterator_datadir/interfaces/guile/metalterator/match.scm
install -p -m0640 -D backend2/meta.scm %buildroot%_alterator_datadir/interfaces/guile/backend/meta.scm
mkdir -p -m0755 %buildroot%_sysconfdir/metalterator
install -p -m0755 -D sbin/metalterator-cmdline %buildroot%_sbindir/metalterator-cmdline

%files
%_alterator_datadir/interfaces/guile/metalterator.scm
%_alterator_datadir/interfaces/guile/metalterator
%_alterator_datadir/interfaces/guile/metalterator/match.scm
%_alterator_datadir/interfaces/guile/backend/meta.scm
%_sysconfdir/metalterator
%_sbindir/metalterator-cmdline

%changelog
* Mon Oct 19 2009  Paul Wolneykien <manowar@altlinux.ru> 1.2-alt3
- Fix object extstence predicate procedure.
- Fix new object creation on simple write operation.

* Fri Aug 28 2009  Paul Wolneykien <manowar@altlinux.ru> 1.2-alt2
- Move direct interface to the metabackend module.

* Sat Aug 18 2009  Paul Wolneykien <manowar@altlinux.ru> 1.2-alt1
- Mapping procedures in queries.

* Thu Jun 25 2009  Paul Wolneykien <manowar@altlinux.ru> 1.1-alt1
- Standalone comand line interface to the Meta backend.

* Tue May 05 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt8
- Use plist-fold instead of unstable plist-filter.

* Fri Apr 24 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt7
- Fix of the wrong macro call.

* Fri Apr 24 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt6
- Fix of the wrong macro call.

* Fri Apr 24 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt5
- Error handling and reporting procedures.

* Wed Apr 22 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt4
- Handling absolute object paths.

* Sat Apr 11 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt3
- Woo-case pattern syntax.

* Thu Apr 09 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- New operations implemented: "link" and "read-next".

* Wed Apr 08 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial release.
