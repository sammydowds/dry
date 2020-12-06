import React, { Component } from "react";
import moment from "moment";
import { Container, Row, Col } from "reactstrap";
import ProjectWorkInProgress from "./sub/ProjectWorkInProgressComponent";
import ProjectDetails from "./sub/ProjectDetailsComponent";
import LeftMenu from "./sub/LeftMenuComponent";
import WelcomeCard from "./sub/WelcomeCardComponent";
import PhasesEndingSoon from "./sub/PhasesEndingSoonComponent";
import RecentChanges from "./sub/RecentChangesComponent";
import CompletedProjects from "./sub/CompletedProjectsComponent";
import Header from "./HeaderComponent";
import ProjectGrid from "./sub/ProjectGridComponent";
import { Redirect } from "react-router-dom";

class renderHome extends Component {
  render() {
    return (
      <Container className="container-spacing home-container" fluid={true}>
        <Header />
        <Row className="h-100 justify-content-center">
          <Col lg="2">
            <LeftMenu
              numProjects={this.props.projects.length}
              projectCreateModal={this.props.projectCreateModal}
              openProjectCreateModal={this.props.openProjectCreateModal}
              closeProjectCreateModal={this.props.closeProjectCreateModal}
              createProject={this.props.createProject}
              logOut={this.props.logOut}
            />
            <CompletedProjects
              projects={this.props.projects}
              projectsLoading={this.props.projectsLoading}
              handleProjectClicked={this.props.openDetails}
              phases={this.props.phases}
              phasesLoading={this.props.phasesLoading}
            />
          </Col>
          <Col className="overflow-auto" lg="5">
            <WelcomeCard
              phases={this.props.phases}
              phasesLoading={this.props.phasesLoading}
              log={this.props.log.filter(
                (entry) =>
                  moment(entry.timestamp, "YYYY-MM-DD") >
                  moment().subtract(48, "hours")
              )}
            />

            {this.props.projectDetails.open ? (
              <ProjectDetails
                project={
                  this.props.projects.filter(
                    (project) =>
                      project.id === this.props.projectDetails.projectId
                  )[0]
                }
                projectsLoading={this.props.projectsLoading}
                phases={this.props.phases.filter(
                  (phase) =>
                    phase.projectId === this.props.projectDetails.projectId
                )}
                phasesLoading={this.props.phasesLoading}
                handleCloseDetails={this.props.closeDetails}
                updateProject={this.props.updateProject}
                updatePhase={this.props.updatePhase}
                createPhase={this.props.createPhase}
                phaseUpdateModal={this.props.phaseUpdateModal}
                phaseCreateModal={this.props.phaseCreateModal}
                projectUpdateModal={this.props.projectUpdateModal}
                openPhaseUpdateModal={this.props.openPhaseUpdateModal}
                closePhaseUpdateModal={this.props.closePhaseUpdateModal}
                openProjectUpdateModal={this.props.openProjectUpdateModal}
                closeProjectUpdateModal={this.props.closeProjectUpdateModal}
                openPhaseCreateModal={this.props.openPhaseCreateModal}
                closePhaseCreateModal={this.props.closePhaseCreateModal}
                createLogEntry={this.props.createLogEntry}
                log={this.props.log.filter(
                  (entry) =>
                    entry.projectId === this.props.projectDetails.projectId
                )}
                deleteProject={this.props.deleteProject}
                deleteSinglePhase={this.props.deleteSinglePhase}
              />
            ) : (
              <React.Fragment>
                <ProjectWorkInProgress
                  projects={this.props.projects}
                  projectsLoading={this.props.projectsLoading}
                  handleProjectClicked={this.props.openDetails}
                  phases={this.props.phases}
                  phasesLoading={this.props.phasesLoading}
                />
              </React.Fragment>
            )}
            <ProjectGrid
              projects={this.props.projects}
              projectsLoading={this.props.projectsLoading}
              handleProjectClicked={this.props.openDetails}
              phases={this.props.phases}
              phasesLoading={this.props.phasesLoading}
              log={this.props.log}
            />
          </Col>
          <Col lg="3">
            <RecentChanges
              log={this.props.log.filter(
                (entry) =>
                  moment(entry.timestamp, "YYYY-MM-DD") >
                  moment().subtract(5, "days")
              )}
              projectsLoading={this.props.projectsLoading}
              projects={this.props.projects}
              phases={this.props.phases}
              handleClicked={this.props.openDetails}
            ></RecentChanges>
            <PhasesEndingSoon
              projectsLoading={this.props.projectsLoading}
              projects={this.props.projects}
              phases={this.props.phases}
              handleClicked={this.props.openDetails}
            ></PhasesEndingSoon>
          </Col>
        </Row>
        {this.props.user.user.authenticated ? (
          <span></span>
        ) : (
          <Redirect to="/login" />
        )}
      </Container>
    );
  }
}

export default renderHome;
