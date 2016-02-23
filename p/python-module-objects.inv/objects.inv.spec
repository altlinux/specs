%define ver 2.3.6
%define reldate 20160223
%define oname objects.inv
Name: python-module-%oname
Version: %ver.%reldate
Release: alt1
Summary: Resource for build documentarion by Sphinx
License: BSD
Group: Development/Python
Url: http://docs.python.org/dev/objects.inv
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source: http://docs.python.org/dev/objects.inv
Source: objects.inv.tar

BuildPreReq: wget rpm-build-python3

%description
This package contains weekly updated Sphinx inventory (version 2,
Project: Python, Version: 3.3) for build documentation by Sphinx.

%package -n python3-module-%oname
Summary: Resource for build documentarion by Sphinx (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
This package contains weekly updated Sphinx inventory (version 2,
Project: Python, Version: 3.3) for build documentation by Sphinx.

%prep
%setup

%build

%install
install -d %buildroot%python_sitelibdir/sphinx
install -m644 objects.inv \
	%buildroot%python_sitelibdir/sphinx

install -d %buildroot%python3_sitelibdir/sphinx
install -m644 objects.inv \
	%buildroot%python3_sitelibdir/sphinx

%files
%dir %python_sitelibdir/sphinx
%python_sitelibdir/sphinx/*

%files -n python3-module-%oname
%dir %python3_sitelibdir/sphinx
%python3_sitelibdir/sphinx/*

%changelog
* Tue Feb 23 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160223-alt1
- repocop cronbuild 20160223. At your service.

* Sat Feb 20 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160220-alt1
- repocop cronbuild 20160220. At your service.

* Sun Feb 14 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160214-alt1
- repocop cronbuild 20160214. At your service.

* Thu Feb 11 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160211-alt1
- repocop cronbuild 20160211. At your service.

* Mon Feb 08 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160208-alt1
- repocop cronbuild 20160208. At your service.

* Sun Feb 07 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160207-alt1
- repocop cronbuild 20160207. At your service.

* Fri Feb 05 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160205-alt1
- repocop cronbuild 20160205. At your service.

* Thu Jan 28 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160128-alt1
- repocop cronbuild 20160128. At your service.

* Sun Jan 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160124-alt1
- repocop cronbuild 20160124. At your service.

* Sun Dec 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151206-alt1
- repocop cronbuild 20151206. At your service.

* Sat Dec 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151205-alt1
- repocop cronbuild 20151205. At your service.

* Thu Dec 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151203-alt1
- repocop cronbuild 20151203. At your service.

* Wed Dec 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151202-alt1
- repocop cronbuild 20151202. At your service.

* Mon Nov 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151130-alt1
- repocop cronbuild 20151130. At your service.

* Sun Nov 29 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151129-alt1
- repocop cronbuild 20151129. At your service.

* Fri Nov 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151127-alt1
- repocop cronbuild 20151127. At your service.

* Thu Nov 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151126-alt1
- repocop cronbuild 20151126. At your service.

* Tue Nov 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151124-alt1
- repocop cronbuild 20151124. At your service.

* Mon Nov 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151123-alt1
- repocop cronbuild 20151123. At your service.

* Sun Nov 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151122-alt1
- repocop cronbuild 20151122. At your service.

* Sat Nov 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151121-alt1
- repocop cronbuild 20151121. At your service.

* Fri Nov 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151120-alt1
- repocop cronbuild 20151120. At your service.

* Thu Nov 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151119-alt1
- repocop cronbuild 20151119. At your service.

* Wed Nov 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151118-alt1
- repocop cronbuild 20151118. At your service.

* Mon Nov 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151116-alt1
- repocop cronbuild 20151116. At your service.

* Sun Nov 15 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151115-alt1
- repocop cronbuild 20151115. At your service.

* Fri Nov 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151113-alt1
- repocop cronbuild 20151113. At your service.

* Tue Nov 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151110-alt1
- repocop cronbuild 20151110. At your service.

* Mon Nov 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151109-alt1
- repocop cronbuild 20151109. At your service.

* Sat Nov 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151107-alt1
- repocop cronbuild 20151107. At your service.

* Fri Nov 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151106-alt1
- repocop cronbuild 20151106. At your service.

* Wed Nov 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151104-alt1
- repocop cronbuild 20151104. At your service.

* Tue Nov 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151103-alt1
- repocop cronbuild 20151103. At your service.

* Mon Nov 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151102-alt1
- repocop cronbuild 20151102. At your service.

* Sun Nov 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151101-alt1
- repocop cronbuild 20151101. At your service.

* Sat Oct 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151031-alt1
- repocop cronbuild 20151031. At your service.

* Thu Oct 29 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151029-alt1
- repocop cronbuild 20151029. At your service.

* Wed Oct 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151028-alt1
- repocop cronbuild 20151028. At your service.

* Mon Oct 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151026-alt1
- repocop cronbuild 20151026. At your service.

* Sun Oct 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151025-alt1
- repocop cronbuild 20151025. At your service.

* Fri Oct 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151023-alt1
- repocop cronbuild 20151023. At your service.

* Thu Oct 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151022-alt1
- repocop cronbuild 20151022. At your service.

* Tue Oct 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151020-alt1
- repocop cronbuild 20151020. At your service.

* Sun Oct 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151018-alt1
- repocop cronbuild 20151018. At your service.

* Sat Oct 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151017-alt1
- repocop cronbuild 20151017. At your service.

* Fri Oct 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151016-alt1
- repocop cronbuild 20151016. At your service.

* Wed Oct 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151014-alt1
- repocop cronbuild 20151014. At your service.

* Tue Oct 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151013-alt1
- repocop cronbuild 20151013. At your service.

* Mon Oct 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151012-alt1
- repocop cronbuild 20151012. At your service.

* Sun Oct 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151011-alt1
- repocop cronbuild 20151011. At your service.

* Sat Oct 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151010-alt1
- repocop cronbuild 20151010. At your service.

* Thu Oct 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151008-alt1
- repocop cronbuild 20151008. At your service.

* Wed Oct 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151007-alt1
- repocop cronbuild 20151007. At your service.

* Tue Oct 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151006-alt1
- repocop cronbuild 20151006. At your service.

* Mon Oct 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151005-alt1
- repocop cronbuild 20151005. At your service.

* Sun Oct 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151004-alt1
- repocop cronbuild 20151004. At your service.

* Fri Oct 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151002-alt1
- repocop cronbuild 20151002. At your service.

* Thu Oct 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20151001-alt1
- repocop cronbuild 20151001. At your service.

* Wed Sep 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150930-alt1
- repocop cronbuild 20150930. At your service.

* Tue Sep 29 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150929-alt1
- repocop cronbuild 20150929. At your service.

* Mon Sep 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150928-alt1
- repocop cronbuild 20150928. At your service.

* Sun Sep 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150927-alt1
- repocop cronbuild 20150927. At your service.

* Mon Sep 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150914-alt1
- repocop cronbuild 20150914. At your service.

* Sun Sep 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150913-alt1
- repocop cronbuild 20150913. At your service.

* Sat Sep 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150912-alt1
- repocop cronbuild 20150912. At your service.

* Thu Sep 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150910-alt1
- repocop cronbuild 20150910. At your service.

* Tue Sep 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150908-alt1
- repocop cronbuild 20150908. At your service.

* Mon Sep 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150907-alt1
- repocop cronbuild 20150907. At your service.

* Sun Sep 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150906-alt1
- repocop cronbuild 20150906. At your service.

* Fri Sep 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150904-alt1
- repocop cronbuild 20150904. At your service.

* Thu Sep 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150903-alt1
- repocop cronbuild 20150903. At your service.

* Wed Sep 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150902-alt1
- repocop cronbuild 20150902. At your service.

* Tue Sep 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150901-alt1
- repocop cronbuild 20150901. At your service.

* Mon Aug 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150831-alt1
- repocop cronbuild 20150831. At your service.

* Sat Aug 29 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150829-alt1
- repocop cronbuild 20150829. At your service.

* Thu Aug 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150827-alt1
- repocop cronbuild 20150827. At your service.

* Wed Aug 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150826-alt1
- repocop cronbuild 20150826. At your service.

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150823-alt1
- repocop cronbuild 20150823. At your service.

* Fri Jul 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150731-alt1
- repocop cronbuild 20150731. At your service.

* Thu Jul 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150730-alt1
- repocop cronbuild 20150730. At your service.

* Thu Jun 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150604-alt1
- repocop cronbuild 20150604. At your service.

* Thu May 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150528-alt1
- repocop cronbuild 20150528. At your service.

* Wed May 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150527-alt1
- repocop cronbuild 20150527. At your service.

* Tue May 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20150526-alt1
- repocop cronbuild 20150526. At your service.

* Mon May 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150525-alt1
- repocop cronbuild 20150525. At your service.

* Sun May 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150524-alt1
- repocop cronbuild 20150524. At your service.

* Sat May 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150523-alt1
- repocop cronbuild 20150523. At your service.

* Fri May 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150522-alt1
- repocop cronbuild 20150522. At your service.

* Thu May 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150521-alt1
- repocop cronbuild 20150521. At your service.

* Wed May 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150520-alt1
- repocop cronbuild 20150520. At your service.

* Tue May 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150519-alt1
- repocop cronbuild 20150519. At your service.

* Mon May 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150518-alt1
- repocop cronbuild 20150518. At your service.

* Sun May 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150517-alt1
- repocop cronbuild 20150517. At your service.

* Sat May 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150516-alt1
- repocop cronbuild 20150516. At your service.

* Fri May 15 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150515-alt1
- repocop cronbuild 20150515. At your service.

* Thu May 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150514-alt1
- repocop cronbuild 20150514. At your service.

* Wed May 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150513-alt1
- repocop cronbuild 20150513. At your service.

* Tue May 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150512-alt1
- repocop cronbuild 20150512. At your service.

* Sun May 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150510-alt1
- repocop cronbuild 20150510. At your service.

* Sat May 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150509-alt1
- repocop cronbuild 20150509. At your service.

* Fri May 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150508-alt1
- repocop cronbuild 20150508. At your service.

* Wed May 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150506-alt1
- repocop cronbuild 20150506. At your service.

* Tue May 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150505-alt1
- repocop cronbuild 20150505. At your service.

* Mon May 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150504-alt1
- repocop cronbuild 20150504. At your service.

* Sun May 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150503-alt1
- repocop cronbuild 20150503. At your service.

* Fri May 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150501-alt1
- repocop cronbuild 20150501. At your service.

* Thu Apr 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150430-alt1
- repocop cronbuild 20150430. At your service.

* Tue Apr 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150428-alt1
- repocop cronbuild 20150428. At your service.

* Mon Apr 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150427-alt1
- repocop cronbuild 20150427. At your service.

* Sun Apr 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150426-alt1
- repocop cronbuild 20150426. At your service.

* Sat Apr 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150425-alt1
- repocop cronbuild 20150425. At your service.

* Fri Apr 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150424-alt1
- repocop cronbuild 20150424. At your service.

* Thu Apr 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150423-alt1
- repocop cronbuild 20150423. At your service.

* Wed Apr 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150422-alt1
- repocop cronbuild 20150422. At your service.

* Tue Apr 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150421-alt1
- repocop cronbuild 20150421. At your service.

* Mon Apr 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150420-alt1
- repocop cronbuild 20150420. At your service.

* Sun Apr 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150419-alt1
- repocop cronbuild 20150419. At your service.

* Fri Apr 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150417-alt1
- repocop cronbuild 20150417. At your service.

* Thu Apr 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150416-alt1
- repocop cronbuild 20150416. At your service.

* Wed Apr 15 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150415-alt1
- repocop cronbuild 20150415. At your service.

* Tue Apr 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150414-alt1
- repocop cronbuild 20150414. At your service.

* Mon Apr 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150413-alt1
- repocop cronbuild 20150413. At your service.

* Sun Apr 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150412-alt1
- repocop cronbuild 20150412. At your service.

* Sat Apr 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150411-alt1
- repocop cronbuild 20150411. At your service.

* Fri Apr 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150410-alt1
- repocop cronbuild 20150410. At your service.

* Thu Apr 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150409-alt1
- repocop cronbuild 20150409. At your service.

* Wed Apr 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150408-alt1
- repocop cronbuild 20150408. At your service.

* Tue Apr 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150407-alt1
- repocop cronbuild 20150407. At your service.

* Mon Apr 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150406-alt1
- repocop cronbuild 20150406. At your service.

* Sun Apr 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150405-alt1
- repocop cronbuild 20150405. At your service.

* Sat Apr 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150404-alt1
- repocop cronbuild 20150404. At your service.

* Fri Apr 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150403-alt1
- repocop cronbuild 20150403. At your service.

* Tue Mar 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150331-alt1
- repocop cronbuild 20150331. At your service.

* Mon Mar 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150330-alt1
- repocop cronbuild 20150330. At your service.

* Sat Mar 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150328-alt1
- repocop cronbuild 20150328. At your service.

* Fri Mar 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150327-alt1
- repocop cronbuild 20150327. At your service.

* Thu Mar 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150326-alt1
- repocop cronbuild 20150326. At your service.

* Tue Mar 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150324-alt1
- repocop cronbuild 20150324. At your service.

* Mon Mar 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150323-alt1
- repocop cronbuild 20150323. At your service.

* Sun Mar 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150322-alt1
- repocop cronbuild 20150322. At your service.

* Sat Mar 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150321-alt1
- repocop cronbuild 20150321. At your service.

* Fri Mar 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150320-alt1
- repocop cronbuild 20150320. At your service.

* Wed Mar 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150318-alt1
- repocop cronbuild 20150318. At your service.

* Tue Mar 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150317-alt1
- repocop cronbuild 20150317. At your service.

* Mon Mar 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150316-alt1
- repocop cronbuild 20150316. At your service.

* Sun Mar 15 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150315-alt1
- repocop cronbuild 20150315. At your service.

* Sat Mar 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150314-alt1
- repocop cronbuild 20150314. At your service.

* Fri Mar 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150313-alt1
- repocop cronbuild 20150313. At your service.

* Thu Mar 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150312-alt1
- repocop cronbuild 20150312. At your service.

* Wed Mar 11 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150311-alt1
- repocop cronbuild 20150311. At your service.

* Tue Mar 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150310-alt1
- repocop cronbuild 20150310. At your service.

* Mon Mar 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150309-alt1
- repocop cronbuild 20150309. At your service.

* Sun Mar 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150308-alt1
- repocop cronbuild 20150308. At your service.

* Sat Mar 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150307-alt1
- repocop cronbuild 20150307. At your service.

* Fri Mar 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150306-alt1
- repocop cronbuild 20150306. At your service.

* Thu Mar 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150305-alt1
- repocop cronbuild 20150305. At your service.

* Wed Mar 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150304-alt1
- repocop cronbuild 20150304. At your service.

* Tue Mar 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150303-alt1
- repocop cronbuild 20150303. At your service.

* Mon Mar 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150302-alt1
- repocop cronbuild 20150302. At your service.

* Sun Mar 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150301-alt1
- repocop cronbuild 20150301. At your service.

* Sat Feb 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150228-alt1
- repocop cronbuild 20150228. At your service.

* Tue Feb 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150224-alt1
- repocop cronbuild 20150224. At your service.

* Mon Feb 23 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150223-alt1
- repocop cronbuild 20150223. At your service.

* Sun Feb 22 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150222-alt1
- repocop cronbuild 20150222. At your service.

* Sat Feb 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150221-alt1
- repocop cronbuild 20150221. At your service.

* Fri Feb 20 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150220-alt1
- repocop cronbuild 20150220. At your service.

* Thu Feb 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150219-alt1
- repocop cronbuild 20150219. At your service.

* Wed Feb 18 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150218-alt1
- repocop cronbuild 20150218. At your service.

* Mon Feb 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150216-alt1
- repocop cronbuild 20150216. At your service.

* Sun Feb 15 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150215-alt1
- repocop cronbuild 20150215. At your service.

* Sat Feb 14 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150214-alt1
- repocop cronbuild 20150214. At your service.

* Fri Feb 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150213-alt1
- repocop cronbuild 20150213. At your service.

* Thu Feb 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150212-alt1
- repocop cronbuild 20150212. At your service.

* Tue Feb 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150210-alt1
- repocop cronbuild 20150210. At your service.

* Mon Feb 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150209-alt1
- repocop cronbuild 20150209. At your service.

* Sun Feb 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150208-alt1
- repocop cronbuild 20150208. At your service.

* Sat Feb 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150207-alt1
- repocop cronbuild 20150207. At your service.

* Fri Feb 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150206-alt1
- repocop cronbuild 20150206. At your service.

* Wed Feb 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150204-alt1
- repocop cronbuild 20150204. At your service.

* Tue Feb 03 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150203-alt1
- repocop cronbuild 20150203. At your service.

* Mon Feb 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150202-alt1
- repocop cronbuild 20150202. At your service.

* Sun Feb 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150201-alt1
- repocop cronbuild 20150201. At your service.

* Sat Jan 31 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150131-alt1
- repocop cronbuild 20150131. At your service.

* Fri Jan 30 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150130-alt1
- repocop cronbuild 20150130. At your service.

* Thu Jan 29 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150129-alt1
- repocop cronbuild 20150129. At your service.

* Wed Jan 28 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150128-alt1
- repocop cronbuild 20150128. At your service.

* Tue Jan 27 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150127-alt1
- repocop cronbuild 20150127. At your service.

* Mon Jan 26 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150126-alt1
- repocop cronbuild 20150126. At your service.

* Sun Jan 25 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150125-alt1
- repocop cronbuild 20150125. At your service.

* Sat Jan 24 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150124-alt1
- repocop cronbuild 20150124. At your service.

* Wed Jan 21 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150121-alt1
- repocop cronbuild 20150121. At your service.

* Mon Jan 19 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150119-alt1
- repocop cronbuild 20150119. At your service.

* Sat Jan 17 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150117-alt1
- repocop cronbuild 20150117. At your service.

* Fri Jan 16 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150116-alt1
- repocop cronbuild 20150116. At your service.

* Tue Jan 13 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150113-alt1
- repocop cronbuild 20150113. At your service.

* Mon Jan 12 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150112-alt1
- repocop cronbuild 20150112. At your service.

* Sat Jan 10 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150110-alt1
- repocop cronbuild 20150110. At your service.

* Fri Jan 09 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150109-alt1
- repocop cronbuild 20150109. At your service.

* Thu Jan 08 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150108-alt1
- repocop cronbuild 20150108. At your service.

* Wed Jan 07 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150107-alt1
- repocop cronbuild 20150107. At your service.

* Tue Jan 06 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150106-alt1
- repocop cronbuild 20150106. At your service.

* Mon Jan 05 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150105-alt1
- repocop cronbuild 20150105. At your service.

* Sun Jan 04 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150104-alt1
- repocop cronbuild 20150104. At your service.

* Fri Jan 02 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150102-alt1
- repocop cronbuild 20150102. At your service.

* Thu Jan 01 2015 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20150101-alt1
- repocop cronbuild 20150101. At your service.

* Tue Dec 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141230-alt1
- repocop cronbuild 20141230. At your service.

* Mon Dec 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141229-alt1
- repocop cronbuild 20141229. At your service.

* Sat Dec 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141227-alt1
- repocop cronbuild 20141227. At your service.

* Fri Dec 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141226-alt1
- repocop cronbuild 20141226. At your service.

* Thu Dec 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141225-alt1
- repocop cronbuild 20141225. At your service.

* Wed Dec 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141224-alt1
- repocop cronbuild 20141224. At your service.

* Tue Dec 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141223-alt1
- repocop cronbuild 20141223. At your service.

* Mon Dec 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141222-alt1
- repocop cronbuild 20141222. At your service.

* Sun Dec 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141221-alt1
- repocop cronbuild 20141221. At your service.

* Sat Dec 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141220-alt1
- repocop cronbuild 20141220. At your service.

* Wed Dec 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141217-alt1
- repocop cronbuild 20141217. At your service.

* Mon Dec 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141215-alt1
- repocop cronbuild 20141215. At your service.

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141213-alt1
- repocop cronbuild 20141213. At your service.

* Fri Dec 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141212-alt1
- repocop cronbuild 20141212. At your service.

* Thu Dec 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141211-alt1
- repocop cronbuild 20141211. At your service.

* Tue Dec 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141209-alt1
- repocop cronbuild 20141209. At your service.

* Mon Dec 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141208-alt1
- repocop cronbuild 20141208. At your service.

* Sat Dec 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141206-alt1
- repocop cronbuild 20141206. At your service.

* Fri Dec 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141205-alt1
- repocop cronbuild 20141205. At your service.

* Wed Dec 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141203-alt1
- repocop cronbuild 20141203. At your service.

* Tue Dec 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141202-alt1
- repocop cronbuild 20141202. At your service.

* Sun Nov 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141130-alt1
- repocop cronbuild 20141130. At your service.

* Sat Nov 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141129-alt1
- repocop cronbuild 20141129. At your service.

* Fri Nov 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141128-alt1
- repocop cronbuild 20141128. At your service.

* Wed Nov 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141126-alt1
- repocop cronbuild 20141126. At your service.

* Mon Nov 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141124-alt1
- repocop cronbuild 20141124. At your service.

* Sun Nov 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141123-alt1
- repocop cronbuild 20141123. At your service.

* Sat Nov 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141122-alt1
- repocop cronbuild 20141122. At your service.

* Fri Nov 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141121-alt1
- repocop cronbuild 20141121. At your service.

* Thu Nov 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141120-alt1
- repocop cronbuild 20141120. At your service.

* Tue Nov 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141118-alt1
- repocop cronbuild 20141118. At your service.

* Mon Nov 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141117-alt1
- repocop cronbuild 20141117. At your service.

* Sat Nov 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141115-alt1
- repocop cronbuild 20141115. At your service.

* Thu Nov 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141113-alt1
- repocop cronbuild 20141113. At your service.

* Tue Nov 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141111-alt1
- repocop cronbuild 20141111. At your service.

* Sat Nov 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141108-alt1
- repocop cronbuild 20141108. At your service.

* Fri Nov 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141107-alt1
- repocop cronbuild 20141107. At your service.

* Wed Nov 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141105-alt1
- repocop cronbuild 20141105. At your service.

* Mon Nov 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141103-alt1
- repocop cronbuild 20141103. At your service.

* Sun Nov 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141102-alt1
- repocop cronbuild 20141102. At your service.

* Sat Nov 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141101-alt1
- repocop cronbuild 20141101. At your service.

* Fri Oct 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141031-alt1
- repocop cronbuild 20141031. At your service.

* Thu Oct 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141030-alt1
- repocop cronbuild 20141030. At your service.

* Tue Oct 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141028-alt1
- repocop cronbuild 20141028. At your service.

* Sat Oct 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141025-alt1
- repocop cronbuild 20141025. At your service.

* Fri Oct 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141024-alt1
- repocop cronbuild 20141024. At your service.

* Wed Oct 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141022-alt1
- repocop cronbuild 20141022. At your service.

* Tue Oct 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141021-alt1
- repocop cronbuild 20141021. At your service.

* Sun Oct 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141019-alt1
- repocop cronbuild 20141019. At your service.

* Sat Oct 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141018-alt1
- repocop cronbuild 20141018. At your service.

* Fri Oct 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141017-alt1
- repocop cronbuild 20141017. At your service.

* Wed Oct 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141015-alt1
- repocop cronbuild 20141015. At your service.

* Mon Oct 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141013-alt1
- repocop cronbuild 20141013. At your service.

* Sun Oct 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141012-alt1
- repocop cronbuild 20141012. At your service.

* Sat Oct 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141011-alt1
- repocop cronbuild 20141011. At your service.

* Fri Oct 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141010-alt1
- repocop cronbuild 20141010. At your service.

* Thu Oct 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141009-alt1
- repocop cronbuild 20141009. At your service.

* Wed Oct 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141008-alt1
- repocop cronbuild 20141008. At your service.

* Mon Oct 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141006-alt1
- repocop cronbuild 20141006. At your service.

* Sat Oct 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141004-alt1
- repocop cronbuild 20141004. At your service.

* Fri Oct 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141003-alt1
- repocop cronbuild 20141003. At your service.

* Wed Oct 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20141001-alt1
- repocop cronbuild 20141001. At your service.

* Tue Sep 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140930-alt1
- repocop cronbuild 20140930. At your service.

* Sun Sep 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140928-alt1
- repocop cronbuild 20140928. At your service.

* Sat Sep 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140927-alt1
- repocop cronbuild 20140927. At your service.

* Fri Sep 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140926-alt1
- repocop cronbuild 20140926. At your service.

* Thu Sep 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140925-alt1
- repocop cronbuild 20140925. At your service.

* Wed Sep 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140924-alt1
- repocop cronbuild 20140924. At your service.

* Mon Sep 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140922-alt1
- repocop cronbuild 20140922. At your service.

* Sun Sep 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140921-alt1
- repocop cronbuild 20140921. At your service.

* Sat Sep 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140920-alt1
- repocop cronbuild 20140920. At your service.

* Fri Sep 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140919-alt1
- repocop cronbuild 20140919. At your service.

* Thu Sep 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140918-alt1
- repocop cronbuild 20140918. At your service.

* Tue Sep 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140916-alt1
- repocop cronbuild 20140916. At your service.

* Mon Sep 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140915-alt1
- repocop cronbuild 20140915. At your service.

* Sat Sep 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140913-alt1
- repocop cronbuild 20140913. At your service.

* Tue Jul 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140708-alt1
- repocop cronbuild 20140708. At your service.

* Sun Jul 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140706-alt1
- repocop cronbuild 20140706. At your service.

* Sat Jul 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140705-alt1
- repocop cronbuild 20140705. At your service.

* Fri Jul 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140704-alt1
- repocop cronbuild 20140704. At your service.

* Thu Jul 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140703-alt1
- repocop cronbuild 20140703. At your service.

* Wed Jul 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140702-alt1
- repocop cronbuild 20140702. At your service.

* Mon Jun 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140630-alt1
- repocop cronbuild 20140630. At your service.

* Sat Jun 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140628-alt1
- repocop cronbuild 20140628. At your service.

* Fri Jun 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140627-alt1
- repocop cronbuild 20140627. At your service.

* Wed Jun 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140625-alt1
- repocop cronbuild 20140625. At your service.

* Tue Jun 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140624-alt1
- repocop cronbuild 20140624. At your service.

* Sun Jun 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140622-alt1
- repocop cronbuild 20140622. At your service.

* Sat Jun 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140621-alt1
- repocop cronbuild 20140621. At your service.

* Wed Jun 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140618-alt1
- repocop cronbuild 20140618. At your service.

* Tue Jun 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140617-alt1
- repocop cronbuild 20140617. At your service.

* Sat Jun 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140614-alt1
- repocop cronbuild 20140614. At your service.

* Fri Jun 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140613-alt1
- repocop cronbuild 20140613. At your service.

* Thu Jun 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140612-alt1
- repocop cronbuild 20140612. At your service.

* Wed Jun 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140611-alt1
- repocop cronbuild 20140611. At your service.

* Mon Jun 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140609-alt1
- repocop cronbuild 20140609. At your service.

* Sun Jun 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140608-alt1
- repocop cronbuild 20140608. At your service.

* Fri Jun 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140606-alt1
- repocop cronbuild 20140606. At your service.

* Thu Jun 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140605-alt1
- repocop cronbuild 20140605. At your service.

* Tue Jun 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140603-alt1
- repocop cronbuild 20140603. At your service.

* Mon Jun 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140602-alt1
- repocop cronbuild 20140602. At your service.

* Sat May 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140531-alt1
- repocop cronbuild 20140531. At your service.

* Fri May 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140530-alt1
- repocop cronbuild 20140530. At your service.

* Wed May 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140528-alt1
- repocop cronbuild 20140528. At your service.

* Tue May 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140527-alt1
- repocop cronbuild 20140527. At your service.

* Sun May 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140525-alt1
- repocop cronbuild 20140525. At your service.

* Sat May 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140524-alt1
- repocop cronbuild 20140524. At your service.

* Fri May 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140523-alt1
- repocop cronbuild 20140523. At your service.

* Thu May 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140522-alt1
- repocop cronbuild 20140522. At your service.

* Wed May 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140521-alt1
- repocop cronbuild 20140521. At your service.

* Mon May 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140519-alt1
- repocop cronbuild 20140519. At your service.

* Sun May 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140518-alt1
- repocop cronbuild 20140518. At your service.

* Fri May 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140516-alt1
- repocop cronbuild 20140516. At your service.

* Thu May 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140515-alt1
- repocop cronbuild 20140515. At your service.

* Tue May 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140513-alt1
- repocop cronbuild 20140513. At your service.

* Mon May 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140512-alt1
- repocop cronbuild 20140512. At your service.

* Sun May 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140511-alt1
- repocop cronbuild 20140511. At your service.

* Sat May 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140510-alt1
- repocop cronbuild 20140510. At your service.

* Fri May 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140509-alt1
- repocop cronbuild 20140509. At your service.

* Wed May 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140507-alt1
- repocop cronbuild 20140507. At your service.

* Tue May 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140506-alt1
- repocop cronbuild 20140506. At your service.

* Sun May 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140504-alt1
- repocop cronbuild 20140504. At your service.

* Sat May 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140503-alt1
- repocop cronbuild 20140503. At your service.

* Fri May 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140502-alt1
- repocop cronbuild 20140502. At your service.

* Thu May 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140501-alt1
- repocop cronbuild 20140501. At your service.

* Wed Apr 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140430-alt1
- repocop cronbuild 20140430. At your service.

* Mon Apr 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140428-alt1
- repocop cronbuild 20140428. At your service.

* Sun Apr 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140427-alt1
- repocop cronbuild 20140427. At your service.

* Fri Apr 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140425-alt1
- repocop cronbuild 20140425. At your service.

* Thu Apr 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140424-alt1
- repocop cronbuild 20140424. At your service.

* Wed Apr 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140423-alt1
- repocop cronbuild 20140423. At your service.

* Mon Apr 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140421-alt1
- repocop cronbuild 20140421. At your service.

* Sat Apr 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140419-alt1
- repocop cronbuild 20140419. At your service.

* Fri Apr 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140418-alt1
- repocop cronbuild 20140418. At your service.

* Wed Apr 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140416-alt1
- repocop cronbuild 20140416. At your service.

* Tue Apr 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140415-alt1
- repocop cronbuild 20140415. At your service.

* Sun Apr 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140413-alt1
- repocop cronbuild 20140413. At your service.

* Sat Apr 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140412-alt1
- repocop cronbuild 20140412. At your service.

* Fri Apr 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140411-alt1
- repocop cronbuild 20140411. At your service.

* Thu Apr 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140410-alt1
- repocop cronbuild 20140410. At your service.

* Wed Apr 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140409-alt1
- repocop cronbuild 20140409. At your service.

* Tue Apr 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140408-alt1
- repocop cronbuild 20140408. At your service.

* Mon Apr 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140407-alt1
- repocop cronbuild 20140407. At your service.

* Sun Apr 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140406-alt1
- repocop cronbuild 20140406. At your service.

* Fri Apr 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140404-alt1
- repocop cronbuild 20140404. At your service.

* Thu Apr 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140403-alt1
- repocop cronbuild 20140403. At your service.

* Wed Apr 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140402-alt1
- repocop cronbuild 20140402. At your service.

* Tue Apr 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140401-alt1
- repocop cronbuild 20140401. At your service.

* Mon Mar 31 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140331-alt1
- repocop cronbuild 20140331. At your service.

* Sun Mar 30 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140330-alt1
- repocop cronbuild 20140330. At your service.

* Sat Mar 29 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140329-alt1
- repocop cronbuild 20140329. At your service.

* Fri Mar 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140328-alt1
- repocop cronbuild 20140328. At your service.

* Wed Mar 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140326-alt1
- repocop cronbuild 20140326. At your service.

* Tue Mar 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140325-alt1
- repocop cronbuild 20140325. At your service.

* Sun Mar 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140323-alt1
- repocop cronbuild 20140323. At your service.

* Sat Mar 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140322-alt1
- repocop cronbuild 20140322. At your service.

* Fri Mar 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140321-alt1
- repocop cronbuild 20140321. At your service.

* Thu Mar 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140320-alt1
- repocop cronbuild 20140320. At your service.

* Wed Mar 19 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140319-alt1
- repocop cronbuild 20140319. At your service.

* Mon Mar 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.5.20140317-alt1
- repocop cronbuild 20140317. At your service.

* Mon Mar 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140317-alt1
- repocop cronbuild 20140317. At your service.

* Sun Mar 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140316-alt1
- repocop cronbuild 20140316. At your service.

* Sat Mar 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140315-alt1
- repocop cronbuild 20140315. At your service.

* Fri Mar 14 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140314-alt1
- repocop cronbuild 20140314. At your service.

* Thu Mar 13 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140313-alt1
- repocop cronbuild 20140313. At your service.

* Tue Mar 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140311-alt1
- repocop cronbuild 20140311. At your service.

* Mon Mar 10 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140310-alt1
- repocop cronbuild 20140310. At your service.

* Sun Mar 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140309-alt1
- repocop cronbuild 20140309. At your service.

* Sat Mar 08 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140308-alt1
- repocop cronbuild 20140308. At your service.

* Fri Mar 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140307-alt1
- repocop cronbuild 20140307. At your service.

* Wed Mar 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140305-alt1
- repocop cronbuild 20140305. At your service.

* Tue Mar 04 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140304-alt1
- repocop cronbuild 20140304. At your service.

* Sun Mar 02 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140302-alt1
- repocop cronbuild 20140302. At your service.

* Sat Mar 01 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140301-alt1
- repocop cronbuild 20140301. At your service.

* Fri Feb 28 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140228-alt1
- repocop cronbuild 20140228. At your service.

* Thu Feb 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140227-alt1
- repocop cronbuild 20140227. At your service.

* Wed Feb 26 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140226-alt1
- repocop cronbuild 20140226. At your service.

* Mon Feb 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140224-alt1
- repocop cronbuild 20140224. At your service.

* Sun Feb 23 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140223-alt1
- repocop cronbuild 20140223. At your service.

* Fri Feb 21 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140221-alt1
- repocop cronbuild 20140221. At your service.

* Thu Feb 20 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140220-alt1
- repocop cronbuild 20140220. At your service.

* Tue Feb 18 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140218-alt1
- repocop cronbuild 20140218. At your service.

* Sun Feb 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140216-alt1
- repocop cronbuild 20140216. At your service.

* Sat Feb 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140215-alt1
- repocop cronbuild 20140215. At your service.

* Wed Feb 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140212-alt1
- repocop cronbuild 20140212. At your service.

* Tue Feb 11 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140211-alt1
- repocop cronbuild 20140211. At your service.

* Sun Feb 09 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140209-alt1
- repocop cronbuild 20140209. At your service.

* Fri Feb 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140207-alt1
- repocop cronbuild 20140207. At your service.

* Thu Feb 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140206-alt1
- repocop cronbuild 20140206. At your service.

* Wed Feb 05 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140205-alt1
- repocop cronbuild 20140205. At your service.

* Mon Feb 03 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140203-alt1
- repocop cronbuild 20140203. At your service.

* Mon Jan 27 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140127-alt1
- repocop cronbuild 20140127. At your service.

* Sat Jan 25 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140125-alt1
- repocop cronbuild 20140125. At your service.

* Fri Jan 24 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140124-alt1
- repocop cronbuild 20140124. At your service.

* Wed Jan 22 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140122-alt1
- repocop cronbuild 20140122. At your service.

* Fri Jan 17 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140117-alt1
- repocop cronbuild 20140117. At your service.

* Thu Jan 16 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140116-alt1
- repocop cronbuild 20140116. At your service.

* Wed Jan 15 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140115-alt1
- repocop cronbuild 20140115. At your service.

* Sun Jan 12 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140112-alt1
- repocop cronbuild 20140112. At your service.

* Tue Jan 07 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140107-alt1
- repocop cronbuild 20140107. At your service.

* Mon Jan 06 2014 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20140106-alt1
- repocop cronbuild 20140106. At your service.

* Tue Dec 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131231-alt1
- repocop cronbuild 20131231. At your service.

* Wed Dec 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131225-alt1
- repocop cronbuild 20131225. At your service.

* Mon Dec 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131223-alt1
- repocop cronbuild 20131223. At your service.

* Sun Dec 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131222-alt1
- repocop cronbuild 20131222. At your service.

* Sat Dec 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131221-alt1
- repocop cronbuild 20131221. At your service.

* Fri Dec 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131220-alt1
- repocop cronbuild 20131220. At your service.

* Tue Dec 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131217-alt1
- repocop cronbuild 20131217. At your service.

* Wed Dec 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131211-alt1
- repocop cronbuild 20131211. At your service.

* Tue Dec 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131210-alt1
- repocop cronbuild 20131210. At your service.

* Sun Dec 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131208-alt1
- repocop cronbuild 20131208. At your service.

* Sat Dec 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131207-alt1
- repocop cronbuild 20131207. At your service.

* Wed Dec 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131204-alt1
- repocop cronbuild 20131204. At your service.

* Mon Dec 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131202-alt1
- repocop cronbuild 20131202. At your service.

* Mon Nov 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131125-alt1
- repocop cronbuild 20131125. At your service.

* Sat Nov 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131123-alt1
- repocop cronbuild 20131123. At your service.

* Fri Nov 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131122-alt1
- repocop cronbuild 20131122. At your service.

* Thu Nov 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131121-alt1
- repocop cronbuild 20131121. At your service.

* Wed Nov 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131120-alt1
- repocop cronbuild 20131120. At your service.

* Tue Nov 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131119-alt1
- repocop cronbuild 20131119. At your service.

* Sat Nov 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131116-alt1
- repocop cronbuild 20131116. At your service.

* Mon Nov 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131111-alt1
- repocop cronbuild 20131111. At your service.

* Fri Nov 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131108-alt1
- repocop cronbuild 20131108. At your service.

* Wed Nov 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131106-alt1
- repocop cronbuild 20131106. At your service.

* Sun Nov 03 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131103-alt1
- repocop cronbuild 20131103. At your service.

* Wed Oct 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131030-alt1
- repocop cronbuild 20131030. At your service.

* Sun Oct 27 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131027-alt1
- repocop cronbuild 20131027. At your service.

* Fri Oct 25 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131025-alt1
- repocop cronbuild 20131025. At your service.

* Wed Oct 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131023-alt1
- repocop cronbuild 20131023. At your service.

* Mon Oct 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131021-alt1
- repocop cronbuild 20131021. At your service.

* Sun Oct 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131020-alt1
- repocop cronbuild 20131020. At your service.

* Fri Oct 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131018-alt1
- repocop cronbuild 20131018. At your service.

* Thu Oct 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131017-alt1
- repocop cronbuild 20131017. At your service.

* Tue Oct 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131015-alt1
- repocop cronbuild 20131015. At your service.

* Mon Oct 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131014-alt1
- repocop cronbuild 20131014. At your service.

* Sat Oct 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131012-alt1
- repocop cronbuild 20131012. At your service.

* Fri Oct 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131011-alt1
- repocop cronbuild 20131011. At your service.

* Wed Oct 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131009-alt1
- repocop cronbuild 20131009. At your service.

* Sun Oct 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131006-alt1
- repocop cronbuild 20131006. At your service.

* Fri Oct 04 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131004-alt1
- repocop cronbuild 20131004. At your service.

* Tue Oct 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20131001-alt1
- repocop cronbuild 20131001. At your service.

* Mon Sep 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130923-alt1
- repocop cronbuild 20130923. At your service.

* Tue Sep 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130917-alt1
- repocop cronbuild 20130917. At your service.

* Sun Sep 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130915-alt1
- repocop cronbuild 20130915. At your service.

* Wed Sep 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130911-alt1
- repocop cronbuild 20130911. At your service.

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130905-alt1
- repocop cronbuild 20130905. At your service.

* Sat Aug 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130831-alt1
- repocop cronbuild 20130831. At your service.

* Fri Aug 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130830-alt1
- repocop cronbuild 20130830. At your service.

* Wed Aug 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130828-alt1
- repocop cronbuild 20130828. At your service.

* Sat Aug 24 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130824-alt1
- repocop cronbuild 20130824. At your service.

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130817-alt1
- repocop cronbuild 20130817. At your service.

* Thu Aug 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130815-alt1
- repocop cronbuild 20130815. At your service.

* Tue Aug 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130813-alt1
- repocop cronbuild 20130813. At your service.

* Sun Aug 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130811-alt1
- repocop cronbuild 20130811. At your service.

* Sat Aug 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130810-alt1
- repocop cronbuild 20130810. At your service.

* Wed Aug 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130807-alt1
- repocop cronbuild 20130807. At your service.

* Tue Aug 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130806-alt1
- repocop cronbuild 20130806. At your service.

* Wed Jul 31 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130731-alt1
- repocop cronbuild 20130731. At your service.

* Mon Jul 29 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130729-alt1
- repocop cronbuild 20130729. At your service.

* Fri Jul 19 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130719-alt1
- repocop cronbuild 20130719. At your service.

* Sun Jul 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130714-alt1
- repocop cronbuild 20130714. At your service.

* Fri Jul 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130712-alt1
- repocop cronbuild 20130712. At your service.

* Mon Jul 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130708-alt1
- repocop cronbuild 20130708. At your service.

* Sat Jul 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130706-alt1
- repocop cronbuild 20130706. At your service.

* Sun Jun 23 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130623-alt1
- repocop cronbuild 20130623. At your service.

* Sat Jun 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130622-alt1
- repocop cronbuild 20130622. At your service.

* Tue Jun 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130618-alt1
- repocop cronbuild 20130618. At your service.

* Sun Jun 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130616-alt1
- repocop cronbuild 20130616. At your service.

* Sat Jun 15 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130615-alt1
- repocop cronbuild 20130615. At your service.

* Fri Jun 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130614-alt1
- repocop cronbuild 20130614. At your service.

* Mon Jun 10 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130610-alt1
- repocop cronbuild 20130610. At your service.

* Sun Jun 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130609-alt1
- repocop cronbuild 20130609. At your service.

* Sat Jun 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130608-alt1
- repocop cronbuild 20130608. At your service.

* Fri Jun 07 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130607-alt1
- repocop cronbuild 20130607. At your service.

* Sun Jun 02 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130602-alt1
- repocop cronbuild 20130602. At your service.

* Sat Jun 01 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130601-alt1
- repocop cronbuild 20130601. At your service.

* Thu May 30 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130530-alt1
- repocop cronbuild 20130530. At your service.

* Tue May 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130528-alt1
- repocop cronbuild 20130528. At your service.

* Sun May 26 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130526-alt1
- repocop cronbuild 20130526. At your service.

* Wed May 22 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130522-alt1
- repocop cronbuild 20130522. At your service.

* Tue May 21 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130521-alt1
- repocop cronbuild 20130521. At your service.

* Sat May 18 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130518-alt1
- repocop cronbuild 20130518. At your service.

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130509-alt1
- repocop cronbuild 20130509. At your service.

* Sun Apr 14 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130414-alt1
- repocop cronbuild 20130414. At your service.

* Sat Apr 13 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130413-alt1
- repocop cronbuild 20130413. At your service.

* Fri Apr 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130412-alt1
- repocop cronbuild 20130412. At your service.

* Thu Apr 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130411-alt1
- repocop cronbuild 20130411. At your service.

* Fri Apr 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.4.20130405-alt1
- repocop cronbuild 20130405. At your service.

* Mon Apr 01 2013 Aleksey Avdeev <solo@altlinux.ru> 2.3.4.20130331-alt1
- Version 2.3.4.20130331

* Wed Mar 20 2013 Aleksey Avdeev <solo@altlinux.ru> 2.3.3.20130320-alt2.1
- Rebuild with Python-3.3

* Wed Mar 20 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20130320-alt2
- repocop cronbuild 20130320. At your service.

* Sat Mar 16 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20130316-alt2
- repocop cronbuild 20130316. At your service.

* Fri Mar 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20130308-alt2
- repocop cronbuild 20130308. At your service.

* Wed Mar 06 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20130306-alt2
- repocop cronbuild 20130306. At your service.

* Thu Feb 28 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20130228-alt2
- repocop cronbuild 20130228. At your service.

* Tue Feb 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20130205-alt2
- repocop cronbuild 20130205. At your service.

* Sat Jan 12 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20130112-alt2
- repocop cronbuild 20130112. At your service.

* Fri Jan 11 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20130111-alt2
- repocop cronbuild 20130111. At your service.

* Tue Jan 08 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20130108-alt2
- repocop cronbuild 20130108. At your service.

* Sat Jan 05 2013 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20130105-alt2
- repocop cronbuild 20130105. At your service.

* Tue Dec 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121225-alt2
- repocop cronbuild 20121225. At your service.

* Thu Dec 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121213-alt2
- repocop cronbuild 20121213. At your service.

* Tue Dec 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121211-alt2
- repocop cronbuild 20121211. At your service.

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121210-alt2
- repocop cronbuild 20121210. At your service.

* Sat Dec 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121208-alt2
- repocop cronbuild 20121208. At your service.

* Wed Dec 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121205-alt2
- repocop cronbuild 20121205. At your service.

* Mon Dec 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121203-alt2
- repocop cronbuild 20121203. At your service.

* Wed Nov 28 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121128-alt2
- repocop cronbuild 20121128. At your service.

* Sat Nov 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121124-alt2
- repocop cronbuild 20121124. At your service.

* Fri Nov 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121123-alt2
- repocop cronbuild 20121123. At your service.

* Wed Nov 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121121-alt2
- repocop cronbuild 20121121. At your service.

* Mon Nov 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121119-alt2
- repocop cronbuild 20121119. At your service.

* Sat Nov 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121117-alt2
- repocop cronbuild 20121117. At your service.

* Sat Nov 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121110-alt2
- repocop cronbuild 20121110. At your service.

* Mon Nov 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121105-alt2
- repocop cronbuild 20121105. At your service.

* Thu Nov 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121101-alt2
- repocop cronbuild 20121101. At your service.

* Wed Oct 31 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121031-alt2
- repocop cronbuild 20121031. At your service.

* Mon Oct 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121022-alt2
- repocop cronbuild 20121022. At your service.

* Thu Oct 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121011-alt2
- repocop cronbuild 20121011. At your service.

* Mon Oct 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121008-alt2
- repocop cronbuild 20121008. At your service.

* Sat Oct 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121006-alt2
- repocop cronbuild 20121006. At your service.

* Fri Oct 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121005-alt2
- repocop cronbuild 20121005. At your service.

* Tue Oct 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121002-alt2
- repocop cronbuild 20121002. At your service.

* Mon Oct 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20121001-alt2
- repocop cronbuild 20121001. At your service.

* Sun Sep 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120923-alt2
- repocop cronbuild 20120923. At your service.

* Sat Sep 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120908-alt2
- repocop cronbuild 20120908. At your service.

* Sat Aug 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120825-alt2
- repocop cronbuild 20120825. At your service.

* Wed Aug 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120822-alt2
- repocop cronbuild 20120822. At your service.

* Mon Aug 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120820-alt2
- repocop cronbuild 20120820. At your service.

* Sun Aug 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120819-alt2
- repocop cronbuild 20120819. At your service.

* Thu Aug 16 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120816-alt2
- repocop cronbuild 20120816. At your service.

* Wed Aug 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120815-alt2
- repocop cronbuild 20120815. At your service.

* Tue Aug 14 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120814-alt2
- repocop cronbuild 20120814. At your service.

* Fri Aug 10 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120810-alt2
- repocop cronbuild 20120810. At your service.

* Thu Aug 09 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120809-alt2
- repocop cronbuild 20120809. At your service.

* Sun Aug 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120805-alt2
- repocop cronbuild 20120805. At your service.

* Sat Aug 04 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120804-alt2
- repocop cronbuild 20120804. At your service.

* Thu Aug 02 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120802-alt2
- repocop cronbuild 20120802. At your service.

* Wed Aug 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120801-alt2
- repocop cronbuild 20120801. At your service.

* Fri Jul 20 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120720-alt2
- repocop cronbuild 20120720. At your service.

* Thu Jul 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120719-alt2
- repocop cronbuild 20120719. At your service.

* Wed Jul 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120718-alt2
- repocop cronbuild 20120718. At your service.

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120717-alt2
- repocop cronbuild 20120717. At your service.

* Fri Jul 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120713-alt2
- repocop cronbuild 20120713. At your service.

* Sun Jun 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120624-alt2
- repocop cronbuild 20120624. At your service.

* Sat Jun 23 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120623-alt2
- repocop cronbuild 20120623. At your service.

* Fri Jun 22 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120622-alt2
- repocop cronbuild 20120622. At your service.

* Sun Jun 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120617-alt2
- repocop cronbuild 20120617. At your service.

* Fri Jun 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120615-alt2
- repocop cronbuild 20120615. At your service.

* Wed Jun 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120613-alt2
- repocop cronbuild 20120613. At your service.

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120612-alt2
- repocop cronbuild 20120612. At your service.

* Fri Jun 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120608-alt2
- repocop cronbuild 20120608. At your service.

* Wed Jun 06 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120606-alt2
- repocop cronbuild 20120606. At your service.

* Tue Jun 05 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120605-alt2
- repocop cronbuild 20120605. At your service.

* Sun Jun 03 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120603-alt2
- repocop cronbuild 20120603. At your service.

* Tue May 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120529-alt2
- repocop cronbuild 20120529. At your service.

* Sun May 27 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120527-alt2
- repocop cronbuild 20120527. At your service.

* Sat May 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120526-alt2
- repocop cronbuild 20120526. At your service.

* Fri May 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120525-alt2
- repocop cronbuild 20120525. At your service.

* Mon May 21 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120521-alt2
- repocop cronbuild 20120521. At your service.

* Sat May 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120519-alt2
- repocop cronbuild 20120519. At your service.

* Fri May 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120518-alt2
- repocop cronbuild 20120518. At your service.

* Tue May 15 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120515-alt2
- repocop cronbuild 20120515. At your service.

* Sun May 13 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120513-alt2
- repocop cronbuild 20120513. At your service.

* Fri May 11 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120511-alt2
- repocop cronbuild 20120511. At your service.

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120508-alt2
- repocop cronbuild 20120508. At your service.

* Tue May 01 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120501-alt2
- repocop cronbuild 20120501. At your service.

* Sun Apr 29 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120429-alt2
- repocop cronbuild 20120429. At your service.

* Thu Apr 26 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120426-alt2
- repocop cronbuild 20120426. At your service.

* Wed Apr 25 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120425-alt2
- repocop cronbuild 20120425. At your service.

* Tue Apr 24 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120424-alt2
- repocop cronbuild 20120424. At your service.

* Thu Apr 19 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120419-alt2
- repocop cronbuild 20120419. At your service.

* Wed Apr 18 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120418-alt2
- repocop cronbuild 20120418. At your service.

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 2.3.3.20120417-alt2
- repocop cronbuild 20120417. At your service.

* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3.20120413-alt2
- Fixed for cronbuild

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3.20120413-alt1
- Added module for Python 3

* Sat Apr 07 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120407-alt1.1
- repocop cronbuild 20120407. At your service.

* Tue Apr 03 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120403-alt1.1
- repocop cronbuild 20120403. At your service.

* Sun Apr 01 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120401-alt1.1
- repocop cronbuild 20120401. At your service.

* Sat Mar 31 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120331-alt1.1
- repocop cronbuild 20120331. At your service.

* Fri Mar 30 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120330-alt1.1
- repocop cronbuild 20120330. At your service.

* Wed Mar 28 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120328-alt1.1
- repocop cronbuild 20120328. At your service.

* Tue Mar 27 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120327-alt1.1
- repocop cronbuild 20120327. At your service.

* Thu Mar 22 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120322-alt1.1
- repocop cronbuild 20120322. At your service.

* Wed Mar 21 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120321-alt1.1
- repocop cronbuild 20120321. At your service.

* Fri Mar 16 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120316-alt1.1
- repocop cronbuild 20120316. At your service.

* Thu Mar 15 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120315-alt1.1
- repocop cronbuild 20120315. At your service.

* Mon Mar 05 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120305-alt1.1
- repocop cronbuild 20120305. At your service.

* Sun Mar 04 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120304-alt1.1
- repocop cronbuild 20120304. At your service.

* Thu Mar 01 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120301-alt1.1
- repocop cronbuild 20120301. At your service.

* Wed Feb 29 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120229-alt1.1
- repocop cronbuild 20120229. At your service.

* Mon Feb 27 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120227-alt1.1
- repocop cronbuild 20120227. At your service.

* Sat Feb 25 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120225-alt1.1
- repocop cronbuild 20120225. At your service.

* Tue Feb 21 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120221-alt1.1
- repocop cronbuild 20120221. At your service.

* Mon Feb 20 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120220-alt1.1
- repocop cronbuild 20120220. At your service.

* Sat Feb 18 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120218-alt1.1
- repocop cronbuild 20120218. At your service.

* Thu Feb 16 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120216-alt1.1
- repocop cronbuild 20120216. At your service.

* Thu Feb 09 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120209-alt1.1
- repocop cronbuild 20120209. At your service.

* Wed Feb 08 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120208-alt1.1
- repocop cronbuild 20120208. At your service.

* Mon Feb 06 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120206-alt1.1
- repocop cronbuild 20120206. At your service.

* Sun Feb 05 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120205-alt1.1
- repocop cronbuild 20120205. At your service.

* Tue Jan 31 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120131-alt1.1
- repocop cronbuild 20120131. At your service.

* Thu Jan 26 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120126-alt1.1
- repocop cronbuild 20120126. At your service.

* Tue Jan 24 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120124-alt1.1
- repocop cronbuild 20120124. At your service.

* Sat Jan 21 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120121-alt1.1
- repocop cronbuild 20120121. At your service.

* Thu Jan 19 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120119-alt1.1
- repocop cronbuild 20120119. At your service.

* Wed Jan 18 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120118-alt1.1
- repocop cronbuild 20120118. At your service.

* Sun Jan 15 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120115-alt1.1
- repocop cronbuild 20120115. At your service.

* Sat Jan 14 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120114-alt1.1
- repocop cronbuild 20120114. At your service.

* Fri Jan 13 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120113-alt1.1
- repocop cronbuild 20120113. At your service.

* Wed Jan 04 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120104-alt1.1
- repocop cronbuild 20120104. At your service.

* Sun Jan 01 2012 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20120101-alt1.1
- repocop cronbuild 20120101. At your service.

* Sat Dec 24 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111224-alt1.1
- repocop cronbuild 20111224. At your service.

* Fri Dec 23 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111223-alt1.1
- repocop cronbuild 20111223. At your service.

* Thu Dec 22 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111222-alt1.1
- repocop cronbuild 20111222. At your service.

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111221-alt1.1
- repocop cronbuild 20111221. At your service.

* Tue Dec 20 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111220-alt1.1
- repocop cronbuild 20111220. At your service.

* Mon Dec 19 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111219-alt1.1
- repocop cronbuild 20111219. At your service.

* Sat Dec 17 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111217-alt1.1
- repocop cronbuild 20111217. At your service.

* Fri Dec 16 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111216-alt1.1
- repocop cronbuild 20111216. At your service.

* Mon Dec 12 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111212-alt1.1
- repocop cronbuild 20111212. At your service.

* Sun Dec 11 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111211-alt1.1
- repocop cronbuild 20111211. At your service.

* Sat Dec 10 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111210-alt1.1
- repocop cronbuild 20111210. At your service.

* Thu Dec 08 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111208-alt1.1
- repocop cronbuild 20111208. At your service.

* Sat Dec 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111203-alt1.1
- repocop cronbuild 20111203. At your service.

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7.20111023-alt1.1
- Rebuild with Python-2.7

* Sun Oct 23 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111023-alt1
- repocop cronbuild 20111023. At your service.

* Thu Oct 20 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111020-alt1
- repocop cronbuild 20111020. At your service.

* Mon Oct 17 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111017-alt1
- repocop cronbuild 20111017. At your service.

* Fri Oct 14 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111014-alt1
- repocop cronbuild 20111014. At your service.

* Wed Oct 12 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20111012-alt1
- repocop cronbuild 20111012. At your service.

* Wed Sep 28 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110928-alt1
- repocop cronbuild 20110928. At your service.

* Mon Sep 19 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110919-alt1
- repocop cronbuild 20110919. At your service.

* Mon Sep 12 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110912-alt1
- repocop cronbuild 20110912. At your service.

* Tue Sep 06 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110906-alt1
- repocop cronbuild 20110906. At your service.

* Sat Sep 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110903-alt1
- repocop cronbuild 20110903. At your service.

* Thu Sep 01 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110901-alt1
- repocop cronbuild 20110901. At your service.

* Tue Aug 23 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110823-alt1
- repocop cronbuild 20110823. At your service.

* Mon Aug 22 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110822-alt1
- repocop cronbuild 20110822. At your service.

* Fri Aug 19 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110819-alt1
- repocop cronbuild 20110819. At your service.

* Sat Aug 13 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110813-alt1
- repocop cronbuild 20110813. At your service.

* Thu Aug 11 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110811-alt1
- repocop cronbuild 20110811. At your service.

* Wed Aug 10 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110810-alt1
- repocop cronbuild 20110810. At your service.

* Mon Aug 08 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110808-alt1
- repocop cronbuild 20110808. At your service.

* Wed Aug 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110803-alt1
- repocop cronbuild 20110803. At your service.

* Sat Jul 30 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110730-alt1
- repocop cronbuild 20110730. At your service.

* Fri Jul 29 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110729-alt1
- repocop cronbuild 20110729. At your service.

* Thu Jul 21 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110721-alt1
- repocop cronbuild 20110721. At your service.

* Mon Jul 18 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110718-alt1
- repocop cronbuild 20110718. At your service.

* Fri Jul 15 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110715-alt1
- repocop cronbuild 20110715. At your service.

* Mon Jul 11 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110711-alt1
- repocop cronbuild 20110711. At your service.

* Sat Jul 09 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110709-alt1
- repocop cronbuild 20110709. At your service.

* Fri Jul 01 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110701-alt1
- repocop cronbuild 20110701. At your service.

* Tue Jun 28 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110628-alt1
- repocop cronbuild 20110628. At your service.

* Mon Jun 27 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110627-alt1
- repocop cronbuild 20110627. At your service.

* Sun Jun 26 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110626-alt1
- repocop cronbuild 20110626. At your service.

* Sat Jun 25 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110625-alt1
- repocop cronbuild 20110625. At your service.

* Mon Jun 20 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110620-alt1
- repocop cronbuild 20110620. At your service.

* Sun Jun 19 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110619-alt1
- repocop cronbuild 20110619. At your service.

* Sat Jun 11 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110611-alt1
- repocop cronbuild 20110611. At your service.

* Fri Jun 10 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110610-alt1
- repocop cronbuild 20110610. At your service.

* Thu Jun 09 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110609-alt1
- repocop cronbuild 20110609. At your service.

* Wed Jun 08 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110608-alt1
- repocop cronbuild 20110608. At your service.

* Mon Jun 06 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110606-alt1
- repocop cronbuild 20110606. At your service.

* Fri Jun 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110603-alt1
- repocop cronbuild 20110603. At your service.

* Thu Jun 02 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110602-alt1
- repocop cronbuild 20110602. At your service.

* Tue May 31 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110531-alt1
- repocop cronbuild 20110531. At your service.

* Sun May 29 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110529-alt1
- repocop cronbuild 20110529. At your service.

* Wed May 25 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110525-alt1
- repocop cronbuild 20110525. At your service.

* Tue May 24 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110524-alt1
- repocop cronbuild 20110524. At your service.

* Mon May 23 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110523-alt1
- repocop cronbuild 20110523. At your service.

* Sun May 15 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110515-alt1
- repocop cronbuild 20110515. At your service.

* Mon May 09 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110509-alt1
- repocop cronbuild 20110509. At your service.

* Sun May 08 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110508-alt1
- repocop cronbuild 20110508. At your service.

* Fri May 06 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110506-alt1
- repocop cronbuild 20110506. At your service.

* Mon May 02 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110502-alt1
- repocop cronbuild 20110502. At your service.

* Sat Apr 30 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110430-alt1
- repocop cronbuild 20110430. At your service.

* Fri Apr 22 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110422-alt1
- repocop cronbuild 20110422. At your service.

* Thu Apr 21 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110421-alt1
- repocop cronbuild 20110421. At your service.

* Wed Apr 20 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110420-alt1
- repocop cronbuild 20110420. At your service.

* Tue Apr 19 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110419-alt1
- repocop cronbuild 20110419. At your service.

* Mon Apr 18 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110418-alt1
- repocop cronbuild 20110418. At your service.

* Fri Apr 15 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110415-alt1
- repocop cronbuild 20110415. At your service.

* Mon Apr 04 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110404-alt1
- repocop cronbuild 20110404. At your service.

* Sun Apr 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110403-alt1
- repocop cronbuild 20110403. At your service.

* Thu Mar 31 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110331-alt1
- repocop cronbuild 20110331. At your service.

* Mon Mar 28 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110328-alt1
- repocop cronbuild 20110328. At your service.

* Thu Mar 24 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110324-alt1
- repocop cronbuild 20110324. At your service.

* Wed Mar 23 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110323-alt1
- repocop cronbuild 20110323. At your service.

* Sun Mar 20 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110320-alt1
- repocop cronbuild 20110320. At your service.

* Fri Mar 18 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110318-alt1
- repocop cronbuild 20110318. At your service.

* Sat Mar 05 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110305-alt1
- repocop cronbuild 20110305. At your service.

* Tue Mar 01 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110301-alt1
- repocop cronbuild 20110301. At your service.

* Sat Feb 26 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110226-alt1
- repocop cronbuild 20110226. At your service.

* Fri Feb 25 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110225-alt1
- repocop cronbuild 20110225. At your service.

* Wed Feb 23 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110223-alt1
- repocop cronbuild 20110223. At your service.

* Tue Feb 22 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110222-alt1
- repocop cronbuild 20110222. At your service.

* Sun Feb 20 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110220-alt1
- repocop cronbuild 20110220. At your service.

* Sat Feb 19 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110219-alt1
- repocop cronbuild 20110219. At your service.

* Tue Feb 15 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110215-alt1
- repocop cronbuild 20110215. At your service.

* Sun Feb 06 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110206-alt1
- repocop cronbuild 20110206. At your service.

* Fri Feb 04 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110204-alt1
- repocop cronbuild 20110204. At your service.

* Sun Jan 30 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110130-alt1
- repocop cronbuild 20110130. At your service.

* Fri Jan 28 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110128-alt1
- repocop cronbuild 20110128. At your service.

* Wed Jan 26 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110126-alt1
- repocop cronbuild 20110126. At your service.

* Tue Jan 25 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110125-alt1
- repocop cronbuild 20110125. At your service.

* Sun Jan 23 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110123-alt1
- repocop cronbuild 20110123. At your service.

* Sun Jan 16 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110116-alt1
- repocop cronbuild 20110116. At your service.

* Fri Jan 14 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110114-alt1
- repocop cronbuild 20110114. At your service.

* Sat Jan 08 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110108-alt1
- repocop cronbuild 20110108. At your service.

* Thu Jan 06 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110106-alt1
- repocop cronbuild 20110106. At your service.

* Mon Jan 03 2011 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20110103-alt1
- repocop cronbuild 20110103. At your service.

* Thu Dec 30 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101230-alt1
- repocop cronbuild 20101230. At your service.

* Tue Dec 28 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101228-alt1
- repocop cronbuild 20101228. At your service.

* Mon Dec 27 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101227-alt1
- repocop cronbuild 20101227. At your service.

* Sun Dec 19 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101219-alt1
- repocop cronbuild 20101219. At your service.

* Sat Dec 18 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101218-alt1
- repocop cronbuild 20101218. At your service.

* Thu Dec 16 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101216-alt1
- repocop cronbuild 20101216. At your service.

* Tue Dec 14 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101214-alt1
- repocop cronbuild 20101214. At your service.

* Mon Dec 13 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101213-alt1
- repocop cronbuild 20101213. At your service.

* Sun Dec 12 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101212-alt1
- repocop cronbuild 20101212. At your service.

* Tue Dec 07 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101207-alt1
- repocop cronbuild 20101207. At your service.

* Sun Dec 05 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101205-alt1
- repocop cronbuild 20101205. At your service.

* Sat Dec 04 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101204-alt1
- repocop cronbuild 20101204. At your service.

* Fri Dec 03 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101203-alt1
- repocop cronbuild 20101203. At your service.

* Thu Dec 02 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101202-alt1
- repocop cronbuild 20101202. At your service.

* Wed Dec 01 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101201-alt1
- repocop cronbuild 20101201. At your service.

* Mon Nov 29 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101129-alt1
- repocop cronbuild 20101129. At your service.

* Sun Nov 28 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101128-alt1
- repocop cronbuild 20101128. At your service.

* Sat Nov 27 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101127-alt1
- repocop cronbuild 20101127. At your service.

* Tue Nov 23 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101123-alt1
- repocop cronbuild 20101123. At your service.

* Mon Nov 22 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101122-alt1
- repocop cronbuild 20101122. At your service.

* Sun Nov 21 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101121-alt1
- repocop cronbuild 20101121. At your service.

* Sat Nov 20 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101120-alt1
- repocop cronbuild 20101120. At your service.

* Fri Nov 19 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101119-alt1
- repocop cronbuild 20101119. At your service.

* Thu Nov 18 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101118-alt1
- repocop cronbuild 20101118. At your service.

* Tue Nov 16 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101116-alt1
- repocop cronbuild 20101116. At your service.

* Tue Nov 09 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101109-alt1
- repocop cronbuild 20101109. At your service.

* Sat Nov 06 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101106-alt1
- repocop cronbuild 20101106. At your service.

* Fri Nov 05 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101105-alt1
- repocop cronbuild 20101105. At your service.

* Tue Nov 02 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101102-alt1
- repocop cronbuild 20101102. At your service.

* Sat Oct 30 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101030-alt1
- repocop cronbuild 20101030. At your service.

* Thu Oct 28 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101028-alt1
- repocop cronbuild 20101028. At your service.

* Tue Oct 26 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101026-alt1
- repocop cronbuild 20101026. At your service.

* Mon Oct 25 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101025-alt1
- repocop cronbuild 20101025. At your service.

* Sun Oct 24 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101024-alt1
- repocop cronbuild 20101024. At your service.

* Sat Oct 23 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101023-alt1
- repocop cronbuild 20101023. At your service.

* Fri Oct 22 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101022-alt1
- repocop cronbuild 20101022. At your service.

* Wed Oct 20 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101020-alt1
- repocop cronbuild 20101020. At your service.

* Sun Oct 17 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101017-alt1
- repocop cronbuild 20101017. At your service.

* Fri Oct 15 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101015-alt1
- repocop cronbuild 20101015. At your service.

* Thu Oct 14 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101014-alt1
- repocop cronbuild 20101014. At your service.

* Wed Oct 13 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101013-alt1
- repocop cronbuild 20101013. At your service.

* Mon Oct 11 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101011-alt1
- repocop cronbuild 20101011. At your service.

* Fri Oct 08 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101008-alt1
- repocop cronbuild 20101008. At your service.

* Wed Oct 06 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101006-alt1
- repocop cronbuild 20101006. At your service.

* Tue Oct 05 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101005-alt1
- repocop cronbuild 20101005. At your service.

* Fri Oct 01 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20101001-alt1
- repocop cronbuild 20101001. At your service.

* Tue Sep 28 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100928-alt1
- repocop cronbuild 20100928. At your service.

* Mon Sep 27 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100927-alt1
- repocop cronbuild 20100927. At your service.

* Thu Sep 23 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100923-alt1
- repocop cronbuild 20100923. At your service.

* Tue Sep 21 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100921-alt1
- repocop cronbuild 20100921. At your service.

* Mon Sep 20 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100920-alt1
- repocop cronbuild 20100920. At your service.

* Sun Sep 19 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100919-alt1
- repocop cronbuild 20100919. At your service.

* Sat Sep 18 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100918-alt1
- repocop cronbuild 20100918. At your service.

* Fri Sep 17 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100917-alt1
- repocop cronbuild 20100917. At your service.

* Wed Sep 15 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100915-alt1
- repocop cronbuild 20100915. At your service.

* Tue Sep 14 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100914-alt1
- repocop cronbuild 20100914. At your service.

* Sat Sep 11 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100911-alt1
- repocop cronbuild 20100911. At your service.

* Fri Sep 10 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100910-alt1
- repocop cronbuild 20100910. At your service.

* Wed Sep 08 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100908-alt1
- repocop cronbuild 20100908. At your service.

* Tue Sep 07 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100907-alt1
- repocop cronbuild 20100907. At your service.

* Mon Sep 06 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100906-alt1
- repocop cronbuild 20100906. At your service.

* Sun Sep 05 2010 Cronbuild Service <cronbuild@altlinux.org> 1.2.7.20100905-alt1
- repocop cronbuild 20100905. At your service.

* Sat Sep 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100904-alt1
- online db update 20100904. At your service.

* Wed Sep 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100901-alt1
- online db update 20100901. At your service.

* Tue Aug 31 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100831-alt1
- online db update 20100831. At your service.

* Sat Aug 28 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100828-alt1
- online db update 20100828. At your service.

* Wed Aug 25 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100825-alt1
- online db update 20100825. At your service.

* Sun Aug 22 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100822-alt1
- online db update 20100822. At your service.

* Thu Aug 19 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100819-alt1
- online db update 20100819. At your service.

* Mon Aug 16 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100816-alt1
- online db update 20100816. At your service.

* Fri Aug 13 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100813-alt1
- online db update 20100813. At your service.

* Tue Aug 10 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100810-alt1
- online db update 20100810. At your service.

* Sat Aug 07 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100807-alt1
- online db update 20100807. At your service.

* Wed Aug 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100804-alt1
- online db update 20100804. At your service.

* Sun Aug 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100801-alt1
- online db update 20100801. At your service.

* Sat Jul 31 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100731-alt1
- online db update 20100731. At your service.

* Wed Jul 28 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100728-alt1
- online db update 20100728. At your service.

* Sun Jul 25 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100725-alt1
- online db update 20100725. At your service.

* Thu Jul 22 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100722-alt1
- online db update 20100722. At your service.

* Mon Jul 19 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100719-alt1
- online db update 20100719. At your service.

* Fri Jul 16 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100716-alt1
- online db update 20100716. At your service.

* Tue Jul 13 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100713-alt1
- online db update 20100713. At your service.

* Sat Jul 10 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100710-alt1
- online db update 20100710. At your service.

* Wed Jul 07 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100707-alt1
- online db update 20100707. At your service.

* Sun Jul 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100704-alt1
- online db update 20100704. At your service.

* Thu Jul 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100701-alt1
- online db update 20100701. At your service.

* Mon Jun 28 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100628-alt1
- online db update 20100628. At your service.

* Fri Jun 25 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100625-alt1
- online db update 20100625. At your service.

* Tue Jun 22 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100622-alt1
- online db update 20100622. At your service.

* Sat Jun 19 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100619-alt1
- online db update 20100619. At your service.

* Wed Jun 16 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100616-alt1
- online db update 20100616. At your service.

* Sun Jun 13 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100613-alt1
- online db update 20100613. At your service.

* Thu Jun 10 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100610-alt1
- online db update 20100610. At your service.

* Mon Jun 07 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100607-alt1
- online db update 20100607. At your service.

* Fri Jun 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100604-alt1
- online db update 20100604. At your service.

* Tue Jun 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100601-alt1
- online db update 20100601. At your service.

* Mon May 31 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100531-alt1
- online db update 20100531. At your service.

* Fri May 28 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100528-alt1
- online db update 20100528. At your service.

* Tue May 25 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100525-alt1
- online db update 20100525. At your service.

* Sat May 22 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100522-alt1
- online db update 20100522. At your service.

* Wed May 19 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100519-alt1
- online db update 20100519. At your service.

* Sun May 16 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100516-alt1
- online db update 20100516. At your service.

* Thu May 13 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100513-alt1
- online db update 20100513. At your service.

* Mon May 10 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100510-alt1
- online db update 20100510. At your service.

* Fri May 07 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100507-alt1
- online db update 20100507. At your service.

* Tue May 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100504-alt1
- online db update 20100504. At your service.

* Sat May 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100501-alt1
- online db update 20100501. At your service.

* Wed Apr 28 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100428-alt1
- online db update 20100428. At your service.

* Sun Apr 25 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100425-alt1
- online db update 20100425. At your service.

* Thu Apr 22 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100422-alt1
- online db update 20100422. At your service.

* Mon Apr 19 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100419-alt1
- online db update 20100419. At your service.

* Fri Apr 16 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100416-alt1
- online db update 20100416. At your service.

* Tue Apr 13 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100413-alt1
- online db update 20100413. At your service.

* Sat Apr 10 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100410-alt1
- online db update 20100410. At your service.

* Wed Apr 07 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100407-alt1
- online db update 20100407. At your service.

* Sun Apr 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100404-alt1
- online db update 20100404. At your service.

* Thu Apr 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100401-alt1
- online db update 20100401. At your service.

* Wed Mar 31 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100331-alt1
- online db update 20100331. At your service.

* Sun Mar 28 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100328-alt1
- online db update 20100328. At your service.

* Thu Mar 25 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100325-alt1
- online db update 20100325. At your service.

* Mon Mar 22 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100322-alt1
- online db update 20100322. At your service.

* Fri Mar 19 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100319-alt1
- online db update 20100319. At your service.

* Tue Mar 16 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100316-alt1
- online db update 20100316. At your service.

* Sat Mar 13 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100313-alt1
- online db update 20100313. At your service.

* Wed Mar 10 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100310-alt1
- online db update 20100310. At your service.

* Sun Mar 07 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100307-alt1
- online db update 20100307. At your service.

* Thu Mar 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100304-alt1
- online db update 20100304. At your service.

* Mon Mar 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100301-alt1
- online db update 20100301. At your service.

* Sat Feb 20 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100220-alt2
- online db update 20100220. At your service.

* Mon Feb 15 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100215-alt2
- online db update 20100215. At your service.

* Tue Feb 09 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100209-alt2
- online db update 20100209. At your service.

* Sun Feb 07 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100207-alt2
- online db update 20100207. At your service.

* Sat Feb 06 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.7.20100206-alt2
- Repocop Q. A. Robot is ready to be promoted to Maintainer Obvious.

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7.20100206-alt1
- Version 1.2.7.20100206

* Thu Feb 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7.20100204-alt1
- Version 1.2.7.20100204

* Sun Jan 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7.20100131-alt1
- Avoided remove comment lines from inventory

* Sat Jan 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7.20100129-alt1
- Initial build for Sisyphus

