%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name: pycairo
Version: 1.8.10
Release: 8%{?dist}
License: MPLv1.1 or LGPLv2
Group: Development/Languages
Summary: Python bindings for the cairo library
URL: http://cairographics.org/pycairo
Source: http://cairographics.org/releases/py2cairo-%{version}.tar.gz

BuildRequires: cairo-devel
BuildRequires: pkgconfig
BuildRequires: python-devel

%description
Python bindings for the cairo library.

%package devel
Summary: Libraries and headers for pycairo
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: cairo-devel
Requires: pkgconfig
Requires: python-devel

%description devel
This package contains files required to build wrappers for cairo add-on
libraries so that they interoperate with pycairo.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' | xargs rm -f

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING* INSTALL NEWS README
%doc examples doc/faq.rst doc/overview.rst doc/README
%{python_sitearch}/cairo/

%files devel
%defattr(-,root,root,-)
%{_includedir}/pycairo/
%{_libdir}/pkgconfig/pycairo.pc

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.8.10-8
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.8.10-7
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.8.10-4
- Revert illegal package rename so it properly builds
- spec file cleanup

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 21 2010 Matthew Barnes <mbarnes@redhat.com> - 1.8.10-1
- Update to 1.8.10
- Rename the package to python-cairo.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Sep 18 2009 Matthew Barnes <mbarnes@redhat.com> - 1.8.8-1
- Update to 1.8.8

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Matthew Barnes <mbarnes@redhat.com> - 1.8.6-1
- Update to 1.8.6

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Matthew Barnes <mbarnes@redhat.com> - 1.8.2-1
- Update to 1.8.2

* Tue Dec 16 2008 Matthew Barnes <mbarnes@redhat.com> - 1.8.0-1
- Update to 1.8.0

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.4.12-5
- Rebuild for Python 2.6

* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.12-4
- fix license tag

* Wed May 07 2008 Matthew Barnes <mbarnes@redhat.com> - 1.4.12-3
- Add more documentation files to the package (RH bug #445519).

* Sun Feb 17 2008 Matthew Barnes <mbarnes@redhat.com> - 1.4.12-2.fc9
- Rebuild with GCC 4.3

* Thu Dec 13 2007 Matthew Barnes <mbarnes@redhat.com> - 1.4.12-1.fc9
- Update to 1.4.12
- Bump cairo requirement to 1.4.12.

* Wed Oct 10 2007 Matthew Barnes <mbarnes@redhat.com> - 1.4.0-2.fc7
- Rebuild

* Thu Mar 15 2007 Matthew Barnes <mbarnes@redhat.com> - 1.4.0-1.fc7
- Update to 1.4.0

* Mon Feb 05 2007 Matthew Barnes <mbarnes@redhat.com> - 1.2.6-3.fc7
- Incorporate suggestions from package review (RH bug #226329).

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 1.2.6-2
- rebuild against python 2.5

* Tue Nov 28 2006 Matthew Barnes <mbarnes@redhat.com> - 1.2.6-1.fc7
- Update to 1.2.6
- Clean up the spec file.

* Sun Oct 15 2006 Matthew Barnes <mbarnes@redhat.com> - 1.2.2-1
- Update to 1.2.2

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.2.0-1.1
- rebuild

* Wed Jul 05 2006 John (J5) Palmieri <johnp@redhat.com> - 1.2.0-1
- Update to upstream 1.2.0

* Mon Jul  3 2006 Jeremy Katz <katzj@redhat.com> - 1.0.2-3
- require new enough cairo (#197457)

* Mon Jun 05 2006 John (J5) Palmieri <johnp@redhat.com> - 1.0.2-2
- add pkgconfig BR

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.2-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.2-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Oct 26 2005 John (J5) Palmieri <johnp@redhat.com> - 1.0.2-1
- Updated to latest and push into rawhide

* Fri Dec 10 2004 Kristian Høgsberg <krh@redhat.com> - 0.1.3-1
- Add python-devel build requires.

* Wed Nov 24 2004  <jrb@redhat.com> - 
- Initial build.
